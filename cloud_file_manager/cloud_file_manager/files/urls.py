from django.contrib import admin
from django.urls import path

from . import views


urlpatterns = [
    path('', views.FileAPIView.as_view(), name='file upload and get lists'),
    path('download/<int:pk>/', views.FileDownloadAPIview.as_view(), name='file download'),
]
