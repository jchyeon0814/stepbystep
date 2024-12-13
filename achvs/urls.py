from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'achvs'

urlpatterns = [
    path("", views.index, name="index")
]
