from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from accounts.models import CustomUser
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post (models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ManyToManyField(Category)
    #tags = models.CharField(max_length=255)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = jmodels.jDateTimeField(null=True)
    created_date = jmodels.jDateTimeField(auto_now_add=True, null=True)
    updated_date = jmodels.jDateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'post'
        verbose_name_plural = 'posts'

    def __str__(self):
        return f"{self.title}-{self.id}"


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=150, null=True, blank=True)
    phone_number = PhoneNumberField(null=False, blank=True)
    subject = models.TextField(max_length=255, null=True, blank=True)
    message = models.TextField()
    approach = models.BooleanField(default=False)
    published_date = jmodels.jDateTimeField(null=True)
    created_date = jmodels.jDateTimeField(auto_now_add=True, null=True)
    updated_date = jmodels.jDateTimeField(auto_now=True, null=True)
    profile_image = models.ImageField(upload_to='profile_image_commenter/', default='profile_image_commenter/default.png')

    def __str__(self):
        return f"{self.name}"