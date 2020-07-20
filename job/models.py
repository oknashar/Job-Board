from django.db import models
# Create your models here.
from django.utils.text import slugify
from django.contrib.auth.models import User
jobType = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)

#coustomizing upload image
def image_upload(instance ,filename):
    imgname , extintion = filename.split('.')
    return 'jobs/%s.%s'%(instance.id,extintion)

class Job(models.Model):
    owner = models.ForeignKey(User,related_name='job_owner',on_delete=models.CASCADE)
    title =models.CharField(max_length=100)
    #location
    job_type = models.CharField(max_length=20,choices=jobType)
    description= models.TextField(max_length=1000)
    published_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    vacancy = models.IntegerField(default=1)
    salary = models.IntegerField(default=0)
    experiance = models.IntegerField(default=1)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,blank=True, null=True)
    image = models.ImageField(upload_to=image_upload)

    slug = models.SlugField(blank=True, null=True)
    class Meta:
        managed = True
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Job, self).save(*args, **kwargs) # Call the real save() method
    
    def __str__(self):
        return self.title





class Category(models.Model):
    
    name =models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name

 
class Apply(models.Model):
    job = models.ForeignKey("Job", related_name='apply_job', on_delete=models.CASCADE)
    name = models.CharField( max_length=50)
    email = models.EmailField(max_length=100)
    website = models.URLField( max_length=200,blank=True, null=True)
    cv = models.FileField(upload_to='apply/',)
    cover_letter  =models.TextField(max_length=500)
    created_at =models.DateTimeField(auto_now=True, auto_now_add=False)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Apply'
        managed = True
        verbose_name = 'Apply'
        verbose_name_plural = 'Applys'