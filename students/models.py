""" Required imports for Students app models """
from django.db import models
from django.contrib.auth.models import User
from courses.models import Course, CourseClass
from schools.models import School

# Create your models here.


class Student(models.Model):
    """
    A class to define the student model including student status
    choices and funding question choices.
    """

    REFERRAL = 'REF'
    STUDENT = 'STD'
    ALUMNI = 'ALM'
    PROGRESSION = 'PRG'
    NO_LONGER_INT = 'NLI'
    status_choices = [
        (REFERRAL, 'Referral'),
        (STUDENT, 'Enrolled'),
        (ALUMNI, 'Alumni'),
        (PROGRESSION, 'Progression'),
        (NO_LONGER_INT, 'No Longer Interested'),
    ]

    JOB_SEEKERS = 'JSA'
    EMP_SUPPORT = 'ESA'
    UNIVERSAL_CREDIT = 'UC'
    INC_SUPPORT = 'ISA'
    COUNCIL_TAX_BENEFIT = 'CTB'
    HOUSING_BENEFIT = 'HB'
    WORKING_TAX_CREDIT = 'WTC'
    PENSION_CREDIT = 'PC'
    NO = 'NO'
    funding_choices = [
        (JOB_SEEKERS, 'Job Seekers Allowance'),
        (EMP_SUPPORT, 'Employability Support Allowance'),
        (UNIVERSAL_CREDIT, 'Universal Credit'),
        (INC_SUPPORT, 'Income Support Allowance'),
        (COUNCIL_TAX_BENEFIT, 'Council Tax Benefit'),
        (HOUSING_BENEFIT, 'Housing Benefit'),
        (WORKING_TAX_CREDIT, 'Working Tax Credit'),
        (PENSION_CREDIT, 'Pension Credit'),
        (NO, 'Not in reciept of benefits')
    ]

    first_name = models.CharField('Forename', max_length=35,)
    last_name = models.CharField('Surname', max_length=35,)
    address_1 = models.CharField("Address line 1", max_length=128,)
    address_2 = models.CharField("Address line 2", max_length=128, blank=True)
    postcode = models.CharField("Postcode", max_length=12,)
    phone = models.CharField("Contact Phone", max_length=15, blank=True)
    email = models.EmailField("Contact Email", max_length=320, blank=True)
    dob = models.DateField("Date of birth", blank=True, default=None)
    school = models.ForeignKey(
        School, null=True, on_delete=models.SET_NULL)
    int_courses = models.ManyToManyField(Course)
    referred_by = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    referral_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    ia_sent = models.BooleanField("Initial Assessment Sent", default=False)
    ia_done = models.BooleanField(
        "Initial Assessment Completed", default=False)
    status = models.CharField(
        choices=status_choices, max_length=3, default=REFERRAL)
    funding = models.CharField(
        choices=funding_choices, max_length=8, default=NO)
    # enrol_num = models.CharField("Student Number", max_length=8, blank=True)
    # enrol_url = models.URLField("Link to myPortal Page", blank=True)
    # courses = models.ManyToManyField(CourseClass, blank=True)
    # prog_course = models.CharField(
    #     "Progression Course Name", max_length=128, blank=True)
    # prog_course_code = models.CharField(
    #     "Progression Course Name", max_length=11, blank=True)
    # prog_course_level = models.CharField(
    #     "Progression Course Code", max_length=15, blank=True)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)
