from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserForm
from django.contrib.auth.models import User
from .models import UserLanguage

@login_required
def home_page(request):
	userlanguage = UserLanguage.objects.get(user=request.user)
	return render(request, 'textmeh/home_page.html', { 'language': userlanguage.language })

def registration(request):
	if request.method == 'POST':
		userform = UserForm(request.POST)
		if userform.is_valid():
			username = userform.cleaned_data['username']
			password = userform.cleaned_data['password']
			language = userform.cleaned_data['language']
			user = User.objects.create_user(username=username, password=password)
			user.save()
			userlanguage = UserLanguage.objects.create(user=user, language=language)
			userlanguage.save()
			return redirect('home_page')
	else:
		userform = UserForm()
	return  render(request, 'textmeh/registration.html', { 'form': userform })