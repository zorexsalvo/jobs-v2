from django.views.generic import ListView 
from django.contrib.auth.models import User
from django.shortcuts import render
from . import models

def populate_content(request):
    jobs_query = models.Job.objects.all()
    return render(request, 'content.html', { 'jobs': jobs_query, 'jobs_count': jobs_query.count() })