from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def news(request):
    return render(request, 'news.html')

def technology(request):
    return render(request, 'Folder/technology.html')

def hr(request):
    return render(request, 'Folder/hr.html')

def Marketing_Technology(request):
    return render(request, 'Folder/marketing_technology.html')

def Machine_Learning(request):
    return render(request, 'Folder/Machine_Learning.html')

def communication(request):
    return render(request, 'Folder/communication.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')