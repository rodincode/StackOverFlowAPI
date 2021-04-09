from django import forms
from .models import Data
from datetime import datetime


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

class Queryform(forms.ModelForm):
    page = forms.IntegerField(required = False)
    pagesize= forms.IntegerField(required = False)
    fromdate= forms.DateField(required = False,widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    todate= forms.DateField(initial=datetime.now().strftime("%Y-%m-%d"),required = False,widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    order= forms.ChoiceField(choices=ORDER_CHOICES,required = False)
    min= forms.DateField(required = False,widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    max= forms.DateField(required = False,widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    sort= forms.ChoiceField(choices=SORT_CHOICES, required = False)
    q= forms.CharField(empty_value = None,required = False)
    accepted= forms.BooleanField(required = False)
    answers= forms.IntegerField(required = False)
    body= forms.CharField(empty_value = None,required = False)
    closed= forms.BooleanField(required = False)
    migrated= forms.BooleanField(required = False)
    notice= forms.BooleanField(required = False)
    nottagged= forms.CharField(empty_value = None,required = False)
    tagged= forms.CharField(empty_value = None,required = False)
    title= forms.CharField(empty_value = None,required = False)
    user= forms.IntegerField(required = False)
    url= forms.CharField(empty_value = None,required = False)
    views= forms.IntegerField(required = False)
    wiki= forms.BooleanField(required = False)
    site= "stackoverflow"
    
    class Meta:
        model=Data
        fields="__all__"
        
# class Feedbackform(ModelForm):
# 	class Meta:
# 		model=Feedback
# 		fields="__all__"
# 		widgets={
# 		"name2":TextInput(attrs={"class":"form-control","placeholder":"Enter Your Company's Name"}),
# 		"review":TextInput(attrs={"class":"form-control","placeholder":"Write your review"}),
        
# 		}


        ##placeholder":"Enter Your Email",   "placeholder":"Enter The Cloth That You Need"