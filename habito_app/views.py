from django.shortcuts import render

from habito_app.models import Habit

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse, HttpResponseBadRequest
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from datetime import datetime
import json


def index(request):
    habit_list = Habit.objects.order_by('title')[:5]
    context_dict = {'habits': habit_list}
    response = render(request, 'habito_app/index.html', context=context_dict)
    return response

def show_user(request):
    habit_list = Habit.objects.order_by('title')[:5]
    context_dict = {'habits': habit_list}
    response = render(request, 'habito_app/test_user.html', context=context_dict)
    return response


def register(request):
    response = render(request, 'habito_app/register.html')
    return response

def login(request):
    response = render(request, 'habito_app/login.html')
    return response

# Shows details of a single habit
def show_habit(request, habit_title_slug):
	try:
		habit = Habit.objects.get(slug=habit_title_slug)

		# This function is used to automatically set to 0 null days from creation date until now
		habit.checkDays()
		# This function is used to check if achievements are completed
		habit.checkAchievements()
		
		# Builds context dict
		context_dict = {
			'habit':habit,
			'habit_title': habit.title, 
			'habit_slug':habit.slug, 
			'habit_desc':habit.description, 
			'days': habit.getDays(),
			'achv': habit.getAchievements()
		}        
	except Habit.DoesNotExist:
		context_dict = {
			'habit':None,
			'habit_desc':None
		}

	response = render(request, 'habito_app/habit.html', context=context_dict)
	return response

# AJAX VIEWS

# Toggles the value (0,1) in the days field and returns the new value
def toogle_day(request):
	day_value = 0
	if request.method == 'GET':
		habit_slug = request.GET['slug']
		day_id = request.GET['day_id']
		habit = Habit.objects.get(slug=habit_slug)
		days = habit.getDays()
		if day_id in days:
			if days[day_id] == 0:
				day_value = 1
			days[day_id] = day_value
			habit.days = json.dumps(days)
			habit.save()
		else:
			return HttpResponseBadRequest()
	return HttpResponse(habit.getDays()[day_id])
	
# Edit the habit's title
def edit_title(request):
	if request.method == 'GET':
		habit_slug = request.GET['slug']
		habit_title = request.GET['new_title']
		habit = Habit.objects.get(slug=habit_slug)
		habit.title = habit_title
		habit.save()
	return HttpResponse(habit.title)