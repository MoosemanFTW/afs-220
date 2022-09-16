from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('bellagio/', views.bellagio, name='bellagio'),
    path('stratosphere/', views.stratosphere, name='stratosphere'),
    path('freemont/', views.freemont, name='freemont')
    # new page path
    # path('pagename/', views.filename, name='pagename')
]