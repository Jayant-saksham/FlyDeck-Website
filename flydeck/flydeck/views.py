from django.shortcuts import HttpResponse, render
from django.views import View
# from google.oauth2 import id_token
# from google.auth.transport import requests
# from django.conf import settings

class IndexView(View):
    template_name = 'index.html'  

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request,*args, **kwargs):
        pass 
    
