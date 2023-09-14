from django.db import models
from django.utils.html import format_html
from tinymce.models import HTMLField
import uuid


# Create your models here.


# creating models category post


class Category(models.Model):
    catId = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    description = HTMLField()
    url = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category/')
    addDate = models.DateTimeField(auto_now_add=True, null=True)

    def get_image(self):
        return format_html(f'<img src="/media/{self.image}"  style="width:30px;height:30px;border-radius:15px"/>')

    def __str__(self):
        return self.title


class Post(models.Model):
    postId = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    description = HTMLField()
    content = models.TextField()
    imageUrl = models.CharField(max_length=256)
    catId = models.ForeignKey(Category, on_delete=models.CASCADE)
    addDate = models.DateTimeField(auto_now_add=True, null=True)

    def get_image(self):
        return format_html(f'<img src="/media/{self.imageUrl}" alt="tempImage"  style="width:30px;height:30px;border-radius:15px"/>')

    def __str__(self):
        return self.title
