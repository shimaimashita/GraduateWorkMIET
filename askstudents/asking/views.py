from django.shortcuts import render

from .models import Mailing, Question, Faculty, Group, Student, Result


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_of_answers = 10
    num_of_completed_mailing = 1
    all_faculties = ' ,'.join(faculty.faculty_name for faculty in Faculty.objects.all())
    all_groups = ' ,'.join(group.group_name for group in Group.objects.all())

    context = {
        'num_of_answers': num_of_answers,
        'num_of_completed_mailing': num_of_completed_mailing,
        'all_faculties': all_faculties,
        'all_groups': all_groups
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
