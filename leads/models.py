from django.db import models
from accounts.models import User

# Create your models here.

class Lead(models.Model):

    name = models.CharField(max_length=200)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=100)

    company_name =  models.CharField(max_length=200,null=True)

    SOURCE_OPTIONS =(
        ("website","Website"),
        ("referral","referral"),
        ("social media","social media"),
        ("advertisement","advertisement"),
        ("other","other")
    )

    source = models.CharField(max_length=100, choices=SOURCE_OPTIONS, default= "other")

    STATUS_CHOICES =(
        ("new","new"),
        ("contacted","contacted"),
        ("interested","interested"),
        ("converted","converted"),
        ("lost","lost"),
    )

    status = models.CharField(max_length=200,choices=STATUS_CHOICES)

    description = models.TextField(null= True)

    created_at = models.DateField(auto_now_add=True)

    updated_at = models.DateField(auto_now_add=True)

    created_by = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):

        return self.name