from django.shortcuts import render
from . import views 

# Create your views here.
def courses(request):
    return render(request, 'courses.html')