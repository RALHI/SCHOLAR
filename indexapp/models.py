from django.db import models

# Create your models here.
class Service(models.Model):
    servicename = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.servicename
