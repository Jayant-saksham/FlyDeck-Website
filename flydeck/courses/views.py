from django.views import View
from django.shortcuts import render, get_object_or_404
from .models import Course, CourseCategory, Video

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


# def video_detail(request, video_id):
#     # Fetch the Video object based on the video_id or any other criteria
#     video = Video.objects.get(pk=video_id)

#     # Create a context dictionary and include the video object
#     context = {
#         'video': video,
#     }

#     # Pass the context to the template
#     return render(request, 'video_detail.html', context)

# def video_detail(request, video_id):
#     # Retrieve the video object based on video_id
#     video = get_object_or_404(Video, pk=video_id)

#     # Retrieve a list of other videos (e.g., related videos)
#     other_videos = Video.objects.exclude(id=video_id)[:5]  # Exclude the current video

#     return render(request, 'video_detail.html', {'video': video, 'other_videos': other_videos})


# def course_videos_side_panel(request, course_slug):
#     # Get the course object using its slug
#     course = get_object_or_404(Course, slug=course_slug)

#     # Get all videos associated with the course
#     course_videos = course.videos.all()

#     context = {
#         'course': course,
#         'course_videos': course_videos,
#     }

#     return render(request, 'course_videos_side_panel.html', context)


# def course_videos_side_panel(request, course_slug, video_id):
#     # Get the course object using its slug
#     course = get_object_or_404(Course, slug=course_slug)

#     # Get the current video based on the video_id
#     current_video = get_object_or_404(course.videos.all(), id=video_id)

#     # Get all videos associated with the course except the current video
#     side_panel_videos = course.videos.exclude(id=video_id)

#     context = {
#         'course': course,
#         'current_video': current_video,
#         'side_panel_videos': side_panel_videos,
#     }

#     return render(request, 'video_detail.html', context)



def video_detail(request, video_id):
    # Retrieve the video object based on video_id
    video = get_object_or_404(Video, pk=video_id)

    # Retrieve a list of other videos (e.g., related videos)
    other_videos = Video.objects.exclude(id=video_id)[:5]  # Exclude the current video

    return render(request, 'video_detail.html', {'video': video, 'other_videos': other_videos})