from django.urls import path
from . import views

urlpatterns = [
    path('',views.myfunctioncall,name="index"),
    path('submitmyform',views.submitmyform,name='submitmyform'),
    path('resume', views.resume,name='resume'),
    path('success', views.success, name='success')
]
