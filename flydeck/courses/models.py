from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField()
    
    def __str__(self):
        return self.title 

class CourseCategory(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField()
    # course_cat_image = models.ImageField(upload_to='course_cat_images/', blank=True, null=True)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Course Categorie'


class Course(models.Model):

    LANGUAGE_CHOICES = (
        ('hn', 'Hindi'),
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('jp', 'Japanese'),
    )

    name = models.CharField(max_length=100)
    course_category = models.ForeignKey(CourseCategory, on_delete=models.CASCADE)
    instructor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    # course_image = models.ImageField(upload_to='course_images/', blank=True, null=True)
    videos = models.ManyToManyField(Video, related_name='courses')
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    slug = models.SlugField(unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name
 


