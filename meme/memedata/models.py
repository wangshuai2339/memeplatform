from django.db import models
from django.contrib.auth.models import AbstractUser
# from  db.base_model import BaseModel

# Create your models here.

class User(AbstractUser):
    avatar = models.ImageField(upload_to="avatars/images", blank=True, null=True)
    class Meta:
        db_table = "user"
        verbose_name = verbose_name_plural = "用户信息表"

class userToken(models.Model):
    username = models.OneToOneField(to="User",on_delete=models.DO_NOTHING)
    token = models.CharField(max_length=60)

    class Meta:
        db_table = "user_token"
        verbose_name = verbose_name_plural = "用户token表"

class TestUser(models.Model):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)

    class Meta:
        db_table = "test_user"
        verbose_name = verbose_name_plural = "测试环境用户信息表"

class TestStar(models.Model):
    username = models.CharField(max_length=32,unique=True)
    password = models.CharField(max_length=32)

    class Meta:
        db_table = "test_star"
        verbose_name = verbose_name_plural = "测试环境主播信息表"


