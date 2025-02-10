from django.shortcuts import render

# Create your views here.
def hisha(request):
	return render(request,'hisha.html')

def skills(request):
	return render(request,'skills.html')

def education(request):
	return render(request,'education.html')

def certified(request):
	return render(request,'certified.html')

def project(request):
	return render(request,'project.html')

def home(request):
	return render(request,'home.html')