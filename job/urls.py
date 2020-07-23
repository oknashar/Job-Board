from django.urls import path

from . import views
from . import api

app_name = 'job'
urlpatterns = [
    path('',views.job_list,name='job_list'),
    path('add',views.addjob,name='add_job'),
    path('<str:slug>',views.job_detail,name='job_det'),
   
   #API
    path('api/list',api.job_list_api,name='job_list_api'),

]
