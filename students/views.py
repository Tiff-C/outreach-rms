""" Import required modules for schools app views """
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Student
from .forms import Add_student
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
        form = Add_student(request.POST)
        if form.is_valid():
            form.save()

            return redirect('referrals')
    form = Add_student()
    context = {
        'form': form
    }
    return render(request, 'students/new_referral.html', context)
