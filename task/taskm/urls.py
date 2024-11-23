from django.urls import path
from . import views
from .views import invite_user

urlpatterns = [
    path('taskm/', views.task_list, name='task_list'),
    path('', views.home, name='home'),
    path('logout', views.logout_view, name='logout'),
    path('create/', views.create_task, name='create_task'), 
    path('update/<int:pk>/', views.update_task, name='update_task'), 
    path('delete/<int:pk>/', views.delete_task, name='delete_task'), 
    path('invite/', invite_user, name='invite_user')
]

