from django.views.generic import ListView
from .models import Job


class JobIndex(ListView):
    model = Job
    template_name = "content.html"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["count"] = self.get_queryset().count()
        return context
