import datetime

from django.db import models
from django.utils import timezone

class User(models.Model): #사용자 테이블
    seq = models.AutoField(primary_key=True)
    user_id = models.CharField(verbose_name="사용자 아이디", max_length=40) ####필드 클래스 반환
    user_nm = models.CharField(verbose_name="사용자명", max_length=40)
    create_dt = models.DateTimeField(verbose_name="생성일", default=timezone.now)
    
    def __str__(self):
        return self.user_id + "(" + self.user_nm + ")"
    
    def was_published_recently(self):
        return self.create_dt >= timezone.now() - datetime.timedelta(days=1)
    
class UserAchv(models.Model): #사용자 성취 테이블
     = models.ForeignKey(User, verbose_name="사용자 아이디", on_delete=models.CASCADE)
    achv_name = models.CharField(verbose_name="목표명", max_length=100)
    achv_max_value = models.PositiveIntegerField(verbose_name="목표값", default=0)
    achv_value = models.PositiveIntegerField(verbose_name="현재값", default=0)
    create_dt = models.DateTimeField(verbose_name="생성일", default=timezone.now)
    update_dt = models.DateTimeField(verbose_name="수정일", null=True, blank=True)
    
    def __str__(self):
        return str(self.user.user_id) + "(" + self.achv_name + ")"

