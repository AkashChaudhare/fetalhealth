from django.contrib import admin
from django.urls import path
from core import views as core_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',core_views.Home.as_view(),name='home'),
    path('diagnose/',core_views.Diagnose.as_view(),name='diagnose'),
    path('about/',core_views.About.as_view(),name='about'),
]
