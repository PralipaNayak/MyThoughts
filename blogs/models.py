from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    img=models.ImageField(upload_to='pics')
    title=models.CharField(max_length=200)
    desc=models.TextField()
    subtitle=models.TextField()
    date=models.DateTimeField(auto_now=True)
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.title + ' | ' + str(self.author)

    # def __str__(self):
    #     return str(self.id)

    # def get_absolue_url(self):
    #     return reverse('index')
    