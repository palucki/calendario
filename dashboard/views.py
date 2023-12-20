from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from cards.models import Calendar

@login_required
def dashboard(request):
    newest_calendars = Calendar.objects.filter(created_by=request.user)[0:5]
    return render(request, 'dashboard/dashboard.html', {
        'newest_calendars': newest_calendars
    })
