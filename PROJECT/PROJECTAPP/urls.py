from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home-pages'),
    path('LPC', views.lpc, name='lpc'),
    path('LPN', views.lpn, name='lpn'),
    path('LPN2', views.lpn2, name='lpn2'),
    path('LPP', views.lpp, name='lpp'),
    path('PST', views.pst, name='pst'),
    path('PST2', views.pst2, name='pst2'),
]