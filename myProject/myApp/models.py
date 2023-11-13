from django.db import models

# Create your models here.
class Person(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField()
    profile_pic=models.ImageField(upload_to='image',null=True,blank=True)

    def __str__(self):
        return self.name