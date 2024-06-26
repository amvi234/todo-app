from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepg'),
    path('register/', views.register, name='register'),
    path('login/', views.loginpage, name='login'),
    path('logout/', views.LogoutView, name='logout'),
    path('delete-task/<str:name>/', views.delete_task, name='delete'),
    path('update/<str:name>/', views.update, name='update'),
]