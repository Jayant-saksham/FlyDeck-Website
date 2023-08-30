from django.shortcuts import render, redirect
from django.views import View
from .models import Contact
from .form import ContactForm

class ContactView(View):
    """
    A view for handling the contact form page.
    """
    template_name = 'contact.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
    def post(self, request, *args, **kwargs):
        form = ContactForm()
        if request.user.is_authenticated:
            form = ContactForm(request.POST)
            if form.is_valid():
                contact_message = Contact(
                user=request.user,
                phone_number = form.cleaned_data['phone_number'],
                message=form.cleaned_data['message'],
                # timestamp = 
                )
                contact_message.save()


                form.save()
                return redirect('contact')
        else:
            print("Login")

        context = {'form': form}
        return render(request,self.template_name, context)
