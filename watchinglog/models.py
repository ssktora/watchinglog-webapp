from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField('メールアドレス', unique=True)

class Team(models.Model):
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.name

class Stadium(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='games', verbose_name="ユーザー", default=None)
    date = models.DateField("観戦日")
    home = models.CharField("ホーム", max_length=30)
    visiter = models.CharField("ビジター", max_length=30)
    stadium = models.CharField("球場", max_length=30)
    home_score = models.PositiveIntegerField("ホームチーム得点")
    visiter_score = models.PositiveIntegerField("ビジターチーム得点")
    memo = models.TextField("感想", blank=True)

    def __str__(self):
        return str(self.date)


# Create your models here.
