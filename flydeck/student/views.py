from django.shortcuts import render, redirect
from django.views import View
from .models import Contact
from .form import ContactForm

class ContactView(View):
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            form.save()
            return redirect('contact')
    
        return render(request,self.template_name, context)
