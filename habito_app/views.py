from django.shortcuts import render

from habito_app.models import Habit

from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

from datetime import datetime

def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    # Get the number of visits to the site.
    # We use the COOKIES.get() function to obtain the visits cookie.
    # If the cookie exists, the value returned is casted to an integer.
    # If the cookie doesn't exist, then the default value of 1 is used.

    # new version - 10.6 chapter
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request,
                                                'last_visit',
                                                str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                                '%Y-%m-%d %H:%M:%S')
                # old version - 10.5
                #visits = int(request.COOKIES.get('visits', '1'))
                #last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
                #last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                #                                    '%Y-%m-%d %H:%M:%S')

        # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
            # update the last visit cookie now that we have updated the count
        # 10.6 chapter
        request.session['last_visit'] = str(datetime.now())
                # 10.5
                #response.set_cookie('last_visit', str(datetime.now()))
    else:
        visits = 1
            # set the last visit cookie
        # 10.6 chapter
        request.session['last_visit'] = last_visit_cookie
                # 10.5
                #response.set_cookie('last_visit', last_visit_cookie)

        # Update/set the visits cookie
    # 10.6 chapter
    request.session['visits'] = visits
                # 10.5
                #response.set_cookie('visits', visits)

def index(request)
    visitor_cookie_handler(request)
    context_dict={}
    context_dict['visits'] = request.session['visits']


    response = render(request, 'habito/index.html', context=context_dict)

    return response

def Habit(request)
    return render(request, 'habito/habit.html')



