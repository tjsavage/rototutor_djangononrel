from django import forms
from django.forms import ModelForm

from users.models import TutorApplication

class TutorApplicationForm(ModelForm):
	class Meta:
		model = TutorApplication
		exclude = ('user',)