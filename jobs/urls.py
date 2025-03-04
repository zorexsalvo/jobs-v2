from django.urls import path
from .views import JobIndex, JobDetail

urlpatterns = [
    path('', JobIndex.as_view(), name='job_index'),
    path('job/<int:pk>/', JobDetail.as_view(), name='job_detail'),
] 
