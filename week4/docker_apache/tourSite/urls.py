from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # new page path
    # path('pagename/', views.filename, name='pagename')
]