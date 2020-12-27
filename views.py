from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.htm')

def about(request):
    return render(request, 'about.htm')

def contact(request):
    return render(request, 'contact.htm')

def addmission(request):
    return render(request, 'add.htm')