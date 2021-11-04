from django.shortcuts import render, redirect
from .models import School, Event
from .forms import Add_school, Add_event
# Create your views here.

def all_schools(request):
    schools = School.objects.all()
    context = {
        'schools': schools
    }
    return render(request, 'schools/schools.html', context)


def all_events(request):
    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'schools/events.html', context)


def add_school(request):
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
