from django.db import models

class Team(models.Model):
    image = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.category}"

class Service(models.Model):
    servicename = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.servicename
    

class UpcomingEvents(models.Model):
    cateory = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Upcoming Events"
        