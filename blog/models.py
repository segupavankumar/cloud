from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class blog(models.Model):
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    # auther = models.CharField(default=User.username,max_length=50)
    title = models.TextField()
    content  = models.TextField()
    date_posted = timezone.localtime(timezone.now())
    img1 = models.ImageField(upload_to='images/',blank=True)
    img2 = models.ImageField(upload_to='images/',blank=True)
    id = models.AutoField(primary_key=True)
