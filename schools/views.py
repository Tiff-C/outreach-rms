from django.shortcuts import render
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
