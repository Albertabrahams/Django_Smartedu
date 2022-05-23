from distutils.command import upload
from email.policy import default
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name= "Kurs Adı", help_text= "Kurs adını yazınız")
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to= "media/%Y %m %d/", default="media/courseisnot.png")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name