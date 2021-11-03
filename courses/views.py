from django.shortcuts import render
from .models import Course, Chapter


def homePage(request):
    courses = Course.objects.all()


    context = {'courses': courses}
    return render(request, 'courses/homePage.html', context)


def viewCourse(request, pk):
    course = Course.objects.filter(id=pk).first()
    content = Chapter.objects.filter(Course_name = course)
    context = {'course': course, 'content': content}
    return render(request, "courses/course_index.html", context)