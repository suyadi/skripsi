from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from jadwal.gcalendar import GCalendar

def home(request):
    context = {}
    gcal = GCalendar(request)
    try:
        context['calendar_list'] = gcal.GetCalendarList()[1]
        context['calendar_resources'] = gcal.GetAllCalendarResources()
        context['sample_resource'] = gcal.GetCalendarResources('-11325871-526')
    except: pass
    return render(request, 'informasi/home.html', context)

def logout(request):
    """Logs out user"""
    auth_logout(request)
    return HttpResponseRedirect('/')
