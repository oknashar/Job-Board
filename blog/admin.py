from django.contrib import admin
from blog import models
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ['created','active']
    list_display = ['title' , 'created','active']
    search_fields = ['title','content']

admin.site.register(models.Post,PostAdmin)