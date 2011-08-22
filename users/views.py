from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from users.forms import TutorApplicationForm

@login_required
def apply(request):
	if request.method == 'POST':
		form = TutorApplicationForm(request.POST)
		if form.is_valid():
			tutorApplication = form.save(commit=False)
			tutorApplication.user = request.user
			tutorApplication.save()
			
			return HttpResponseRedirect('/apply/thanks')
	else:
		form = TutorApplicationForm()
		
	return render_to_response("apply.html", {"form":form})

@login_required
def me(request):
	return HttpResponse("hi")