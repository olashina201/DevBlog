from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field
  

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(default='', upload_to='upload')
    genre = models.ForeignKey(Category, default='coding', on_delete=models.CASCADE)
    #content = RichTextField(blank=True, null=True)
    content = CKEditor5Field('Text', config_name='extends')
    date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    