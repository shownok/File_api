from django.urls import path, include
from .import views


urlpatterns = [
    path('list/', views.tfileupload, name='file-list'),
    path('create', views.tCreate, name='create-list'),
    path('update/<str:pk>', views.update, name='update-list'),
]