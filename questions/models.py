from django.db import models
from django.utils import timezone
# Create your models here.

SORT_CHOICES = ( 
    ("activity", "activity"), 
    ("votes", "votes"), 
    ("creation", "creation"), 
    ("relevance", "relevance"), 
    )

ORDER_CHOICES = ( 
    ("desc", "desc"), 
    ("asc", "asc"), 
    )
class Data(models.Model):
        page = models.IntegerField(default = None, null = True,blank=True)
        pagesize= models.IntegerField(default = None, null = True,blank=True)
        fromdate= models.DateField(default = None, null = True,blank=True)
        todate= models.DateField(default = None, null = True,blank=True)
        order= models.CharField(max_length= 30,choices=ORDER_CHOICES,default = None, null = True,blank=True)
        min= models.DateField(default = None, null = True,blank=True)
        max= models.DateField(default = None, null = True,blank=True)
        sort= models.CharField(max_length= 30,choices=SORT_CHOICES, default = None, null = True,blank=True)
        q= models.CharField(max_length=1000,default = None, null = True,blank=True)
        accepted= models.BooleanField(default = False, null = True,)
        answers= models.IntegerField(default = None, null = True,blank=True)
        body= models.CharField(max_length=1000,default = None, null = True,blank=True)
        closed= models.BooleanField(default = False, null = True,)
        migrated= models.BooleanField(default = False, null = True,)
        notice= models.BooleanField(default = False, null = True,)
        nottagged= models.CharField(max_length=1000,default = None, null = True,blank=True)
        tagged= models.CharField(max_length=1000,default = None, null = True,blank=True)
        title= models.CharField(max_length=1000,default = None, null = True,blank=True)
        user= models.IntegerField(default = None, null = True,blank=True)
        url= models.CharField(max_length=1000,default = None, null = True,blank=True)
        views= models.IntegerField(default = None, null = True,blank=True)
        wiki= models.BooleanField(default = False, null = True,)
        site= "stackoverflow"

        def __str__(self):
            return self.site

# #Soham@1234