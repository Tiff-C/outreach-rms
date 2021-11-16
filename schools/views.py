""" Import required modules for schools app views """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import School, Event
from .forms import Add_school, Add_event
# Create your views here.


@login_required
def all_schools(request):
    """ A view to show all schools """

    schools = School.objects.all()
    context = {
        'schools': schools
    }
    return render(request, 'schools/schools.html', context)


@login_required
def all_events(request):
    """ A view to show all events """

    events = Event.objects.all()
    context = {
        'events': events
    }
    return render(request, 'schools/events.html', context)


@login_required
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


@login_required
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


@login_required
def school_details(request, school_id):
    """ A view to show school details """
    school = get_object_or_404(School, pk=school_id)

    context = {
        'school': school,
    }

    return render(request, 'schools/school_details.html', context)


@login_required
def event_details(request, event_id):
    """ A view to show event details """
    event = get_object_or_404(Event, pk=event_id)

    context = {
        'event': event,
    }

    return render(request, 'schools/event_details.html', context)


@login_required
def edit_school(request, school_id):
    """ A view to edit a school """
    school = get_object_or_404(School, pk=school_id)
    
    if request.method == 'POST':
        form = Add_school(request.POST, instance=school)
        if form.is_valid():
            form.save()

            return redirect('schools')

    form = Add_school(instance=school)
    context = {
        'form': form,
        'school': school
    }
    return render(request, 'schools/edit_school.html', context)


@login_required
def delete_school(request, school_id):
    """ A view to delete a school """
    school = get_object_or_404(School, pk=school_id)
    school.delete()
    return redirect('schools')


@login_required
def edit_event(request, event_id):
    """ A view to edit an event """
    event = get_object_or_404(Event, pk=event_id)
    
    if request.method == 'POST':
        form = Add_event(request.POST, instance=event)
        if form.is_valid():
            form.save()

            return redirect('events')

    form = Add_event(instance=event)
    context = {
        'form': form,
        'event': event
    }
    return render(request, 'schools/edit_event.html', context)


@login_required
def delete_event(request, event_id):
    """ A view to delete an event """
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return redirect('events')