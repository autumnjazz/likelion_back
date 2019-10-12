from django.db import models
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label="Your name", max_length=100)  # ,widget = forms.Textarea

# Create your models here.
class Question(models.Model):
    question_text= models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    question_id = models.ForeignKey(Question,on_delete=models.CASCADE)      #ForeignKey
    choice_text = models.CharField(max_length = 200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
