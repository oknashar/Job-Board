from django.db import models

# Create your models here.

jobType = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)
class Job(models.Model):

    title =models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=20,choices=jobType)
    description= models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experiance = models.IntegerField(default=1)



    def __str__(self):
        return self.title

