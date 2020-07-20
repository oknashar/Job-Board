from django.db import models
# Create your models here.
from django.utils.text import slugify
jobType = (
    ('Full Time','Full Time'),
    ('Part Time','Part Time')
)

#coustomizing upload image
def image_upload(instance ,filename):
    imgname , extintion = filename.split('.')
    return 'jobs/%s.%s'%(instance.id,extintion)

class Job(models.Model):

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

 
