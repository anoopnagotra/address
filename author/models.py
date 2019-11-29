from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Author(models.Model):
    first_name = models.CharField( max_length=200, default="", verbose_name="FIRST NAME")
    last_name = models.CharField( max_length=200, default="", verbose_name="LAST NAME")
    biography = models.TextField( max_length=2000, default="", verbose_name="BIOGRAPHY")
    facebook_url = models.URLField(verbose_name="FACEBOOK URL", null=True, blank=True)
    linkedin_url = models.URLField(null=True, blank=True)
    google_plus_url = models.URLField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    author_image = models.ImageField(upload_to='author/')
    image_gallery = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name + self.last_name

