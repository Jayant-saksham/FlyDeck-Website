from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.CourseView.as_view(), name='courses'),
    # path('course-details/', views.course_details, name='course-details'),
] 
