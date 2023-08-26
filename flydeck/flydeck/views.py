# views.py
from django.shortcuts import HttpResponse, render
# from google.oauth2 import id_token
# from google.auth.transport import requests
# from django.conf import settings

def index(request):
    return render(request, 'index.html')
    
