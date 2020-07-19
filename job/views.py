from django.shortcuts import render
from .models import Job
# Create your views here.

def job_list(request):
    jobList = Job.objects.all()

    context = {
        'jobs':jobList
    }
    return render(request,'job_list.html',context)

def job_detail(request,id):
    job_det = Job.objects.get(id=id)
    context = {'job':job_det}
    return render(request,'job_detail.html',context)
