from django.shortcuts import render
from .models import Course


def homePage(request):
    courses = Course.objects.all()

    mem = courses.get(id='daa540ca0e5445b898bb9c6c543032bb')
    print(mem)
    context = {'courses': courses}
    return render(request, 'courses/homePage.html', context)
