from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request , 'index.html')

def skills(request):
    return render(request , 'skills.html')

def project(request):
    return render(request , 'project.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')