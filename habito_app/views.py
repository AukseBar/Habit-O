from django.shortcuts import render

from habito_app.models import Habit

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from datetime import datetime


def index (request):
    context_dict={}
    response = render(request, 'habito_app/index.html')

    return response

def Habit(request):
    response=render(request, 'habito_app/habit.html')
    return response



