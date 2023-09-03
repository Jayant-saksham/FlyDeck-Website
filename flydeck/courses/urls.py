from django.urls import path
from . import views

urlpatterns = [
    path(r'', views.CourseView.as_view(), name='courses'),
    path('video/<int:video_id>/', views.video_detail, name='video_detail'),
    # path('<slug:course_slug>/<int:video_id>/', views.video_detail, name='video_detail'),
    # path('<slug:course_slug>/<int:video_id>/', views.course_videos_side_panel, name='course_videos_side_panel'),
    # path('video/<int:video_id>/', views.video_detail, name='video_detail'),
] 
