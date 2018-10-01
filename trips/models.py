from django.db import models
from django import forms

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    photo = models.URLField(blank=True)
    location = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    travel_date = models.DateField('旅遊日期',null=False)

    def __str__(self):
        return self.title

class mes_board(forms.Form):
    bname = forms.CharField()
    bcontent = forms.CharField()
    bcreated_time = forms.DateTimeField(auto_now_add=True)
