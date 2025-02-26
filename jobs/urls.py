from django.urls import path
from .views import JobIndexView

urlpatterns = [
    path('', JobIndexView.as_view(), name='job_index'),
] 