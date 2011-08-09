from django.db import models
from django.contrib.auth.models import User

class Tutor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    bio = models.TextField(blank=True)
    address = models.TextField()
    phone = models.CharField(max_length=12)
    active = models.BooleanField(default=False)
    application = models.ForeignKey('TutorApplication', null=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class TutorApplication(models.Model):
    pass

class Client(models.Model):
    user = models.ForeignKey(User, null=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    parent_first_name = models.CharField(max_length=30, blank=True)
    parent_last_name = models.CharField(max_length=30, blank=True)

    def __unicode__(self):
        return self.first_name + " " + self.last_name

class TutorClientPair(models.Model):
    """
    For suggestions for clients matching with tutors
    """
    tutor = models.ForeignKey('Tutor')
    client = models.ForeignKey('Client')

