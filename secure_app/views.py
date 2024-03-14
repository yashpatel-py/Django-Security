from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'secure_app/index.html')
def register(request):
    return render(request, 'secure_app/register.html')
def dashboard(request):
    return render(request, 'secure_app/dashboard.html')