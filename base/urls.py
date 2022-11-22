from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index,name="index"),
    path('details/<str:id>/', views.details, name="details"),
    path('create/', views.create_task, name="create_task"),
    path('update/<str:id>/', views.update_task, name="update_task"),
    path('delete/<str:id>/', views.delete_task, name="delete_task"),
    path('account/login/', views.login_page, name="login"),
    path('account/register/', views.register_page, name="register"),
    path('account/logout/', views.logout_page, name="logout"),
    path('search/', views.search, name="searchposts"),
    path('account-page/' , views.account_page, name='account-page')
]

