from django.shortcuts import render,redirect
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm,JobForm
from django.urls import reverse
# Create your views here.

def job_list(request):
    jobList = Job.objects.all()

    paginator = Paginator(jobList, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'jobs':page_obj
    }
    return render(request,'jobs.html',context)

def job_detail(request,slug):
    job_det = Job.objects.get(slug=slug)
    if request.method =='POST':
        form = ApplyForm(request.POST,request.FILES)
        if form.is_valid:
            myform = form.save(commit=False)
            myform.job =job_det
            myform.save()
        
    else:
        form = ApplyForm()
    context = {'job':job_det,'form':form}
    return render(request,'job_details.html',context)

def addjob(request):
    if request.method=='POST':
        form = JobForm(request.POST ,request.FILES)

        if form.is_valid:
            myform = form.save(commit=False)
            myform.owner =request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))
    else:
        form =JobForm()
    context={'form':form}
    return render(request,'add_job.html',context)