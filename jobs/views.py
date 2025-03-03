from django.views.generic import ListView 
from django.contrib.auth.models import User
from django.shortcuts import render
from . import models

def populate_content(request):
    job_query = models.Job.objects.all()
    print(job_query)
    return render(request, 'content.html', { 'jobs': job_query })