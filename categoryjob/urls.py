
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('customer_job_show/', views.customer_job_showing),
    path('human_job_show/', views.human_job_showing),
    path('management_job_show/', views.management_job_showing),
    path('development_job_show/', views.development_job_showing),
    path('sales_job_show/', views.sales_job_showing),
    path('teaching_job_show/', views.teaching_job_showing),
    path('design_job_show/', views.design_job_showing),
]
