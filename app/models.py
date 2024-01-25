from django.db import models
from django.contrib.auth.models import User
# to save slug automatically 
from django.template.defaultfilters import slugify

# create the models her:

# Create category class:--------------------- start the categroy model
class Category(models.Model):
    categroy_name = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.categroy_name
#-------------------------------------------- end the categroy model    
    
# Create post class:-------------------------- start the post model
class Post(models.Model):
    # relationship btween user and Post class  
    auther = models.ForeignKey(User, on_delete= models.CASCADE) 
    # relationship btween Categroy and Post class 
    category = models.ForeignKey(Category, on_delete= models.SET_NULL, null=True,related_name='categroy') 
    title = models.CharField(max_length=200)
    descrption = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    slug = models.CharField(max_length=200, blank=True , null= True)
    # relationship btween user and Post class  
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    # like counts
    like_counts = models.PositiveIntegerField(default=0)

    #--- disply string title in admen 
    def __str__(self):
        return self.title

    # to take title and put it insid the slug field auto:<----> start function to fild title in insid automatically    
    def save(self,*args,**kwargs):
       self.slug = slugify(self.title)
       # *args this mean can take so many argaments 
       # **kwargs this mean can take so many objects
       # super that mean can custmos on inhert class
       super(Post,self).save(*args,**kwargs)
    #------------------------------------------------ end the fild title slug function
       
    # her to add counts like:--------- start the cunte like function
    def update_like_counts(self):
        self.like_counts = self.likes.count()
        self.save()
    #------------------------------------------------ end the cunte function
               
#-----------------------------------------------------end the post model         

# comment system post models:------------------- start the comment models
class PostComment(models.Model):
    auther = models.ForeignKey(User,on_delete = models.SET_NULL, null=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add= True)
    
    # make the object human readabel
    def __str__(self):
        return f'{self.post} - {self.description}'
#--------------------------------------------------- end the models


class NestedComment(models.Model):
    auther = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    nested_comment = models.ForeignKey(PostComment, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.comment} - {self.nested_comment}'

