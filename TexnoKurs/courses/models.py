from django.db import models
from teachers.models import Teacher
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, null=True, unique=True)
    def __str__(self):
        return self.name 


class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, null=True, unique=True)

    def __str__(self):
        return self.name


class Course(models.Model):
    teacher = models.ForeignKey(Teacher, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, unique=True, verbose_name="Course name")
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    tags = models.ManyToManyField(Tag, blank=True, null=True)
    students = models.ManyToManyField(User, blank=True, related_name='courses_joined')
    description = RichTextField(blank=True, null=True)
    image = models.ImageField(upload_to="courses/%Y/%m/%d/", default="courses/default_image.png")
    date = models.DateTimeField(auto_now=True)
    available = models.BooleanField(default=True)
    course_price = models.CharField(null=False,max_length=3)

    def __str__(self):
        return self.name
    

class Comment(models.Model):
    article = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="comments", verbose_name="Course")
    comment_author = models.CharField(max_length=50, verbose_name="Author")
    comment_content = models.TextField(max_length=200,verbose_name="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_author