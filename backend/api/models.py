from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    website = models.URLField(blank=True)

class Speaker(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    bio = models.TextField()

class Session(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    speaker = models.ForeignKey(Speaker, on_delete=models.CASCADE)
    time = models.DateTimeField()
