from django.urls import path
from .views import IndexView,GameDetailView,WatchingCreate,WatchingUpdate,WatchingDelete
from django.contrib.auth.decorators import login_required

app_name = "watchinglog"
urlpatterns = [
    path("", login_required(IndexView.as_view()), name="index"),
    path("game/<int:pk>/", login_required(GameDetailView.as_view()), name="detail"),
    path("create/", login_required(WatchingCreate.as_view()), name="create"),#これ追加
    path("update/<int:pk>", login_required(WatchingUpdate.as_view()), name="update"),#これ追加
    path("delete/<int:pk>", login_required(WatchingDelete.as_view()), name="delete"), #これ追加
]