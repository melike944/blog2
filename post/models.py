from django.db import models

# Create your models here.
class post(models.Model):
    title=models.CharField(max_length=64)
    content=models.TextField()
    image=models.ImageField(upload_to="post/image/",null=True)
    datetime=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
