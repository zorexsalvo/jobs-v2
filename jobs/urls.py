from django.urls import path
from . import views

urlpatterns = [
    path('', views.populate_content, name='job_index'),
] 