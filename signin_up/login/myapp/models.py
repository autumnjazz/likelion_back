from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.TextField()
    phone_number = models.TextField(verbose_name="폰번호")

    # def __str__(self):
    #     return self.user

    #default unique verbose_name help_text db_index blank null