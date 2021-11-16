""" Import required modules for use in courses app views """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course
from .forms import Add_course

# Create your views here.


@login_required
def all_courses(request):
    """ A view to show all courses """
    courses = Course.objects.all()
    context = {
        'courses': courses
    }
    return render(request, 'courses/courses.html', context)


@login_required
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


@login_required
def course_details(request, course_id):
    """ A view to show course details """
    course = get_object_or_404(Course, pk=course_id)

    context = {
        'course': course,
    }

    return render(request, 'courses/course_details.html', context)
