""" Import required modules for schools app views """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import StudentForm
# Create your views here.


@login_required
def all_referrals(request):
    """ A view to show all current referrals """

    referrals = Student.objects.all()
    context = {
        'referrals': referrals
    }
    return render(request, 'students/referrals.html', context)


@login_required
def add_referral(request):
    """ A view to add a new referral """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('referrals')
    form = StudentForm()
    context = {
        'form': form
    }
    return render(request, 'students/new_referral.html', context)


@login_required
def referral_details(request, student_id):
    """ A view to show student details """
    referral = get_object_or_404(Student, pk=student_id)

    context = {
        'referral': referral,
    }

    return render(request, 'students/referral_details.html', context)
