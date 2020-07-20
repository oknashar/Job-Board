from django.shortcuts import render
from .models import Job
from django.core.paginator import Paginator
from .forms import ApplyForm
# Create your views here.

def job_list(request):
    jobList = Job.objects.all()

    paginator = Paginator(jobList, 1)
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
