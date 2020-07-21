from django.conf.urls import url
from django.urls import include,path
from . import views
#for Second API

app_name = 'Post'
urlpatterns = [
    path('',views.all_post,name='all_post'),
    path('<int:id>' , views.post ,name='post'),
    path('create/',views.create_post,name='create_post'),
    path('<int:id>/edit' , views.edit_post ,name='edit_post'),


]
