import datetime

from django.db import models
from django.utils import timezone
from users.models import User

# Create your models here.
class UserAchv(models.Model): #사용자 성취 테이블
    user_ref = models.ForeignKey(User, verbose_name="사용자키", on_delete=models.CASCADE)
    achv_name = models.CharField(verbose_name="목표명", max_length=100)
    achv_max_value = models.PositiveIntegerField(verbose_name="목표값", default=0)
    achv_value = models.PositiveIntegerField(verbose_name="현재값", default=0)
    create_dt = models.DateTimeField(verbose_name="생성일", default=timezone.now)
    update_dt = models.DateTimeField(verbose_name="수정일", null=True, blank=True)
    
    def __str__(self):
        return str(self.user_seq) + "(" + self.achv_name + ")"