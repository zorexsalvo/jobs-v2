from django.views.generic import ListView, DetailView
from django.db.models import Q
from .models import Job


class JobIndex(ListView):
    model = Job
    template_name = "content.html"
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', '')
        if search_query:
            queryset = queryset.filter(
                Q(title__icontains=search_query) |
                Q(company_name__icontains=search_query)
            )
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job_count"] = self.get_queryset().count()
        context["company_count"] = Job.objects.values('company_name').distinct().count()
        context["search_query"] = self.request.GET.get('search', '')
        return context

class JobDetail(DetailView):
    model = Job
    template_name = "job_detail.html"
    context_object_name = 'job'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add related jobs from the same company
        context["related_jobs"] = Job.objects.filter(
            company_name=self.object.company_name
        ).exclude(id=self.object.id)[:3]
        return context
