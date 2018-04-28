from django.urls import path

from jobs import views as jobviews
from .views import CompanyHome

urlpatterns = [
    path('job/delete/<int:pk>/', jobviews.JobDelete.as_view(extra_context={'title': 'Delete Job'}), name='job_delete'),
    path('job/update/<int:pk>/', jobviews.JobUpdate.as_view(extra_context={'title': 'Update Job'}), name='job_update'),
    path('job/create/', jobviews.JobCreate.as_view(extra_context={'title': 'Create Job'}), name='job_create'),
    path('job/<int:pk>', jobviews.JobsByCompanyDetail.as_view(), name='company_job_detail'),
    path('jobs/', jobviews.JobsByCompany.as_view(), name='company_jobs'),
    path('home/', CompanyHome.as_view(), name='company_home'),
]