from django.views.generic import ListView 
from django.contrib.auth.models import User


class JobIndexView(ListView):
    model = User
    template_name = "index.html"
