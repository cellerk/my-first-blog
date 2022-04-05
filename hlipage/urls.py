from django.urls import path

from . import views

urlpatterns = [
    #path('', views.index, name='index'),
    #path('', views.button, name='home'),
    path('', views.post_new, name='home'),
    path('output', views.output, name='script'),
    path('download', views.download, name='download')
]