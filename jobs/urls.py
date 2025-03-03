from django.urls import path
from .views import JobIndex

urlpatterns = [
    path('', JobIndex.as_view(), name='job_index'),
] 
