from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	context = {}
	return render(request, 'info/index.html', context)

def about(request):
	context = {}
	return render(request, 'info/about.html', context)

def resume(request):
	context = {}
	return render(request, 'info/resume.html', context)

def contact(request):
	context = {}
	return render(request, 'info/contact.html', context)
