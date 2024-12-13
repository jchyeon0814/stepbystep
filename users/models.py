import datetime

from django.db import models
from django.utils import timezone

class User(models.Model): #사용자 테이블
    user_id = models.CharField(verbose_name="사용자 아이디", max_length=40) ####필드 클래스 반환
    user_nm = models.CharField(verbose_name="사용자명", max_length=40)
    create_dt = models.DateTimeField(verbose_name="생성일", default=timezone.now)
    
    def __str__(self):
        return self.user_id + "(" + self.user_nm + ")"
    
    def was_published_recently(self):
        return self.create_dt >= timezone.now() - datetime.timedelta(days=1)
    
