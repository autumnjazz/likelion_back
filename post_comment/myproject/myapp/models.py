from django.db import models
from django.utils import timezone 

class Post(models.Model):
    title = models.CharField(max_length= 100)
    contents = models.TextField()
    pub_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-id'] #id의 역순으로 순서

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE) 
    #foreignkey 는 일대다 관계. post와 comment의 관계
    content = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.content
    
    class Meta:
        ordering = ['-id'] #id의 역순으로 순서