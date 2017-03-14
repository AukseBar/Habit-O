from django.shortcuts import render

from habito_app.models import Habit

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from datetime import datetime


def index(request):
    habit_list = Habit.objects.order_by('title')[:5]
    context_dict = {'habits': habit_list}
    response = render(request, 'habito_app/index.html', context=context_dict)
    return response


def show_habit(request, habit_title_slug):
    context_dict = {}

    try:

        habit = Habit.objects.get(slug=habit_title_slug)

        context_dict['habit'] = habit
    except Habit.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -

        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None

    response = render(request, 'habito_app/habit.html', context=context_dict)
    return response

