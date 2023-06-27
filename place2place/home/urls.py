"""
URL configuration for home app.
"""

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name='homepage'),
    path('makeorder/', views.makeorder,name='makeorderspage'),
    path('vieworders/', views.vieworders,name='vieworderspage'),
    path('estimateprices/', views.estimateprices,name='estimatepricespage'),
    path('logout/', views.logout,name='logoutpage'),
    path('register/', views.register,name='registerpage'),
    path('login/', views.login,name='loginpage'),
]
