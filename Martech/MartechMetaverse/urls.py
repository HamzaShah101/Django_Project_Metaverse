from django.contrib import admin
from django.urls import path,include
from MartechMetaverse import views

urlpatterns = [
    path("",views.index,name="home"),
    path("news",views.news,name="news")
]