from django.contrib import admin
from django.urls import path,include
from MartechMetaverse import views

urlpatterns = [
    path("",views.index,name="home"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("technology",views.technology,name="technology"),
    path("hr",views.hr,name="hr"),
    path("Marketing Technology",views.Marketing_Technology,name="marketing_technology"),
    path("Machine Learning",views.Machine_Learning,name="Machine Learning"),
    path("Communication",views.communication,name="Communication"),
]