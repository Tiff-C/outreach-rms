""" Import required modules for schools app views """
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from courses.models import CourseClass
from .models import Student
from .forms import ReferralForm, StudentForm
# Create your views here.


@login_required
def all_referrals(request):
    """ A view to show all current referrals """

    referrals = Student.objects.filter(status='REF')
    context = {
        'referrals': referrals
    }
    return render(request, 'students/referrals.html', context)


@login_required
def all_students(request):
    """ A view to show all current students """

    students = Student.objects.filter(status='STD')
    context = {
        'students': students
    }
    return render(request, 'students/students.html', context)


@login_required
def add_referral(request):
    """ A view to add a new referral """
    if request.method == 'POST':
        form = ReferralForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('referrals')
    form = ReferralForm()
    context = {
        'form': form
    }
    return render(request, 'students/new_referral.html', context)


@login_required
def add_student(request, student_id):
    """
    A view to convert a referral to a student.
    Redirects back to referrals page to allow user to add
    another student.
    """
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

            return redirect('referrals')

    form = StudentForm(instance=student)
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'students/add_student.html', context)


@login_required()
def edit_referral(request, student_id):
    """ A view to edit a referral """
    referral = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        form = ReferralForm(request.POST, instance=referral)
        if form.is_valid():
            form.save()

            return redirect('referrals')

    form = ReferralForm(instance=referral)
    context = {
        'form': form,
        'referral': referral
    }
    return render(request, 'students/edit_referral.html', context)


@login_required
def edit_student(request, student_id):
    """ A view to edit a student """
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()

            return redirect('students')

    form = StudentForm(instance=student)
    context = {
        'form': form,
        'student': student
    }
    return render(request, 'students/edit_student.html', context)


@login_required
def delete_referral(request, student_id):
    """ A view to delete a referral """
    referral = get_object_or_404(Student, pk=student_id)
    referral.delete()
    return redirect('referrals')


@login_required
def delete_student(request, student_id):
    """ A view to delete a student """
    student = get_object_or_404(Student, pk=student_id)
    student.delete()
    return redirect('students')


@login_required
def referral_details(request, student_id):
    """ A view to show referral details """
    referral = get_object_or_404(Student, pk=student_id)

    context = {
        'referral': referral,
    }

    return render(request, 'students/referral_details.html', context)


@login_required
def student_details(request, student_id):
    """
    A view to show student details and the courses they
    are enrolled on.
    """
    student = get_object_or_404(Student, pk=student_id)

    context = {
        'student': student,
    }

    return render(request, 'students/student_details.html', context)
