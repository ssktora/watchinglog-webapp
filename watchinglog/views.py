from django.shortcuts import render
from django.views.generic import TemplateView, ListView,DetailView,UpdateView,DeleteView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Game
from django.core.mail import send_mail
from django.http import HttpResponse

from .forms import SignUpForm, activate_user, GameForm

# def emailfunc(request):
#     send_mail(
#         "タイトル",
#         "本文",
#         "送信元のメールアドレス",
#         ["送信元のメールアドレス"],
#         fail_silently=False,
#     )
#     return HttpResponse('')

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ActivateView(TemplateView):
    template_name = "registration/activate.html"
    
    def get(self, request, uidb64, token, *args, **kwargs):
        result = activate_user(uidb64, token)
        return super().get(request, result=result, **kwargs)

class IndexView(LoginRequiredMixin,ListView):
    model = Game
    context_object_name = 'game_list'
    def get_queryset(self):
        return Game.objects.filter(user=self.request.user)

class GameDetailView(DetailView):
    model = Game
    context_object_name = 'game'

class WatchingCreate(CreateView):
    model = Game
    form_class = GameForm  # GameFormを指定
    template_name = 'watchinglog/game_form.html'
    success_url = reverse_lazy("watchinglog:index")

    def form_valid(self, form):
        # user フィールドを現在ログインしているユーザーに設定
        form.instance.user = self.request.user
        return super().form_valid(form)

class WatchingUpdate(UpdateView):
    model = Game
    form_class = GameForm  # GameFormを指定
    template_name = 'watchinglog/game_form.html'
    success_url = reverse_lazy("watchinglog:index")# "index" に修正
    def get_form_kwargs(self):
        kwargs = super(WatchingUpdate, self).get_form_kwargs()
        kwargs['instance'] = self.object  # 編集対象のGameモデルを渡す
        return kwargs

class WatchingDelete(DeleteView):
    model = Game
    context_object_name = "game"
    success_url = reverse_lazy("watchinglog:index")