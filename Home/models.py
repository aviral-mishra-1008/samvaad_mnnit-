from django.db import models

# Create your models here.
from django.db import models

class Submissions(models.Model):
    name = models.CharField(max_length=100, default = "" )
    email_id = models.CharField(max_length=1000, default="")
    heading = models.CharField(max_length=100, default="An article")
    estimated_time = models.IntegerField(default=0, null=True)
    article = models.TextField(max_length=10000000000000000000000,default="")
    image = models.ImageField(upload_to="media/",default="",null=True)
    linked_in = models.CharField(max_length=10000, default="")
    insta = models.CharField(max_length=1000,default='')
    youtube = models.CharField(max_length=10000, default='')
    reg_no = models.IntegerField(default=0, null=True)
    branch = models.CharField(max_length = 100, default="")
    year = models.IntegerField(default=0, null=True)
    phone_no = models.IntegerField(default=0, null = True)
    unique_identifier = models.IntegerField(default = 0, null = True)
    art = models.CharField(max_length=10000000000000000000000000, default="")

    def __str__(self):
        return self.name
class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name= models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone= models.CharField(max_length=20)
    query=models.TextField()

    def __str__(self):
        return self.name

    