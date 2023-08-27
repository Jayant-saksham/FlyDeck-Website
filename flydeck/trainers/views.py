from django.shortcuts import render

# Create your views here.
def trainers(request):
    return render(request, 'trainers.html')