from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_all_classroom),
    path('create-classroom/', views.create_classroom),
]