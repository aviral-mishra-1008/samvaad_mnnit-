from django.db import models

# Create your models here.
from django.db import models

class Submissions(models.Model):
    unique_id = models.IntegerField(default = 0, null = True)
    name = models.CharField(max_length=100, default = "" )
    email_id = models.CharField(max_length=1000, default="")
    heading = models.CharField(max_length=1000, default="An article")
    estimated_time = models.IntegerField(default=0, null=True)
    article = models.TextField(max_length=1000000,default="")
    image = models.ImageField(upload_to="",default="",null=True)
    insta = models.CharField(max_length=1000,default='')
    reg_no = models.BigIntegerField(default=0, null=True)
    branch = models.CharField(max_length = 100, default="")
    year = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    date= models.DateField(auto_now=True)
    email = models.CharField(max_length=100)
    phone= models.CharField(max_length=20)
    image = models.ImageField(upload_to="contact_image/",default="",null=True)
    query=models.TextField()

    def __str__(self):
        return self.email

    
class Post(models.Model):
    name = models.CharField(max_length=100, default = "" )
    email_id = models.CharField(max_length=1000, default="")
    heading = models.CharField(max_length=1000, default="An article")
    estimated_time = models.IntegerField(default=0, null=True)
    article = models.TextField(max_length=1000000,default="")
    image = models.ImageField(upload_to="",default="")
    branch = models.CharField(max_length = 100, default="")
    year = models.IntegerField(default=0, null=True)
    slug=models.CharField(max_length=130)
    unique_identifier = models.BigIntegerField(default=0, null=True )
    

    def __str__(self):
        return self.name