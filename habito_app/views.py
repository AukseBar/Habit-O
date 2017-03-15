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
    response = render(request, 'habito_app/test_index.html', context=context_dict)
    return response

def show_user(request):
    habit_list = Habit.objects.order_by('title')[:5]
    context_dict = {'habits': habit_list}
    response = render(request, 'habito_app/test_user.html', context=context_dict)
    return response


def show_habit(request, habit_title_slug):
    context_dict = {}

    try:
        habit = Habit.objects.get(slug=habit_title_slug)
        days = habit.getDays()
        description = habit.description

        #build dic for days
        context_dict['habit'] = habit
        context_dict['description'] = description
        #context_dict['days'] = days
        print description
        print days
    except Habit.DoesNotExist:
        context_dict['habit'] = None
        context_dict['description'] = None

    response = render(request, 'habito_app/test_habit.html', context=context_dict)
    return response

