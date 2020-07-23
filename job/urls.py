from django.urls import path

from . import views
from . import api

app_name = 'job'
urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add',views.addjob,name='add_job'),
    path('<str:slug>',views.job_detail,name='job_det'),
   
   #API
    path('api/jobs',api.job_list_api,name='job_list_api'),
    path('api/jobs/<int:id>',api.job_detail_api,name='job_detail_api'),


    # class based views
    path('api/v2/jobs',api.JobListApi.as_view(),name= 'job_list_api'),
    path('api/v2/jobs/<int:id>',api.JobDetailApi.as_view(),name= 'job_detail_api')
]
