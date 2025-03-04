from django.views.generic import ListView, DetailView
from django.db.models import Q, Count, Max
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

class CompanyList(ListView):
    model = Job
    template_name = "companies.html"
    context_object_name = 'companies'

    def get_queryset(self):
        # Get unique companies with their job counts and latest job
        companies = (
            Job.objects.values('company_name')
            .annotate(
                job_count=Count('id'),
                latest_job=Max('created_at')
            )
            .order_by('company_name')
        )
        return companies

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get the latest job for each company
        company_jobs = {}
        for company in context['companies']:
            latest_jobs = Job.objects.filter(
                company_name=company['company_name']
            ).order_by('-created_at')[:3]
            company_jobs[company['company_name']] = latest_jobs
        context['company_jobs'] = company_jobs
        return context
