from django.db import models


# Create your models here.
class Post(models.Model):
    name = models.CharField(max_length=100, default = "" )
    email_id = models.CharField(max_length=1000, default="")
    heading = models.CharField(max_length=100, default="An article")
    estimated_time = models.IntegerField(default=0, null=True)
    article = models.CharField(max_length=1000000000000000000,default="")
    image = models.ImageField(upload_to="",default="")
    branch = models.CharField(max_length = 100, default="")
    year = models.IntegerField(default=0, null=True)
    slug=models.CharField(max_length=130)
    unique_identifier = models.IntegerField(default=0, null=True )
    

    def __str__(self):
        return self.name