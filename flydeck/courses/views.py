from django.views import View
from django.shortcuts import render
from .models import Course, CourseCategory

# Create your views here.

class CourseView(View):
    template_name = 'courses.html' 

    def get(self, request, *args, **kwargs):
        courses = Course.objects.all()
        context = {'course': courses}
        return render(request, self.template_name, context)
    
    def post(self, request, *args, **kwargs):
        pass

    

class CourseDetail(View):
    template_name = 'course-details.html'  

    def get(self, request, *args, **kwargs):
        courses = Course.object.all()
        context = {'course': courses}
        return render(request, self.template_name, context)
    
    def post(self, request,*args, **kwargs):
        pass 


