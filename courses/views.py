""" Import required modules for use in courses app views """
from django.shortcuts import render, redirect
from .models import Course
from .forms import Add_course
# Create your views here.


def all_courses(request):
    """ A view to show all courses """
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses/courses.html', context)


def add_course(request):
    """ A view to add a new course """
    if request.method == 'POST':
        form = Add_course(request.POST)
        if form.is_valid():
            form.save()

            return redirect('courses')
    form = Add_course()
    context = {
        'form': form
    }
    return render(request, 'courses/add_course.html', context)
