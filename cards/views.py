from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse, Http404

from .forms import CalendarForm, CardForm
from .models import Calendar, Card

def index(request):
    return HttpResponse("Hello, world. You're at the calendars index.")

# @login_required
def cards(request, calendar_id):
    cards = get_list_or_404(Card, calendar__id=calendar_id)

    return render(request, 'cards/cards.html', {
        'cards': cards,
    })

    # print(request.GET.get('id'))
    # cards = Card.objects.filter(available_at__lte = datetime.datetime.now())

@login_required
def create_card(request):
    if request.method == 'POST':
        form = CardForm(request.POST)

        if form.is_valid():
            card = form.save(commit=False)
            card.created_by = request.user
            card.save()

            return redirect('/dashboard/')
    else:
        form = CardForm()
        form.fields['calendar'].queryset = Calendar.objects.filter(created_by=request.user)

    return render(request, 'cards/create_card.html', {
        'form': form,
    })

@login_required
def create_calendar(request):
    if request.method == 'POST':
        form = CalendarForm(request.POST)

        if form.is_valid():
            calendar = form.save(commit=False)
            calendar.created_by = request.user
            calendar.save()

            return redirect('/dashboard/')
    else:
        form = CalendarForm()

    return render(request, 'cards/create_calendar.html', {
        'form': form,
    })