from django.db import models
from django.contrib.auth.models import User
from lib.form_fields import MultiSelectField
import settings


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
	user = models.ForeignKey(User)
	previous_experience = models.TextField(verbose_name="Do you have any previous tutoring or teaching experience?")
	hear_about = models.TextField(verbose_name="How'd you hear about RotoTutor")
	car = models.BooleanField(verbose_name="I have a car.")
	date_added = models.DateTimeField(auto_now_add=True)
#	subjects = MultiSelectField(choices=settings.SUBJECTS)

	def __unicode__(self):
		return self.user.first_name + " " + self.user.last_name + " Application on " + str(self.date_added)

class Subjects(models.Model):
	name = models.CharField(max_length=60)

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

