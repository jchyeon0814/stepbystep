import datetime

from django.db import models
from django.utils import timezone

class User(models.Model): #사용자 테이블
    user_id = models.CharField(max_length=40) ####필드 클래스 반환
    user_nm = models.CharField(max_length=40)
    create_dt = models.DateTimeField("date published")
    
    def __str__(self):
        return self.user_id + "(" + self.user_nm + ")"
    
    def was_published_recently(self):
        return self.create_dt >= timezone.now() - datetime.timedelta(days=1)
    
class UserAchv(models.Model): #사용자 성취 테이블
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    achv_name = models.CharField(max_length=100)
    achv_max_value = models.PositiveIntegerField(default=0)
    achv_value = models.PositiveIntegerField(default=0)
    create_dt = models.DateTimeField("date published")
    update_dt = models.DateTimeField("date published")
    
    def __str__(self):
        return self.user_id + "(" + self.achv_name + ")"

