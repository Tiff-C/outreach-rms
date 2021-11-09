""" Import required modules for schools app views """
from django.shortcuts import render, redirect
from .models import School, Event
from .forms import Add_school, Add_event
# Create your views here.


def all_schools(request):
    """ A view to show all schools """

    schools = School.objects.all()
    context = {
        'schools': schools
    }
    return render(request, 'schools/schools.html', context)


def all_events(request):
    """ A view to show all events """

    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'schools/events.html', context)


def add_school(request):
    """ A view to add a school """
    if request.method == 'POST':
        form = Add_school(request.POST)
        if form.is_valid():
            form.save()

            return redirect('schools')
    form = Add_school()
    context = {
        'form': form
    }
    return render(request, 'schools/add_school.html', context)


def add_event(request):
    """ A view to add an event """
    if request.method == 'POST':
        form = Add_event(request.POST)
        if form.is_valid():
            form.save()

            return redirect('events')
    form = Add_event()
    context = {
        'form': form
    }
    return render(request, 'schools/add_event.html', context)
