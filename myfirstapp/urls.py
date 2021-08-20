from django.urls import path
from . import views

urlpatterns = [
    path('',views.resume,name="resume"),
    path('submitmyform',views.submitmyform,name='submitmyform'),
    path('resume', views.resume,name='resume'),
    path('success', views.success, name='success')
]
