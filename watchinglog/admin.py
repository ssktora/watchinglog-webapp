from django.contrib import admin
from watchinglog.models import Game, Team, Stadium, User
# Register your models here.
admin.site.register(Team)
admin.site.register(Stadium)
admin.site.register(Game)
admin.site.register(User)