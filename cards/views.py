import random

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
    
    # hardcoded randomization
    random.shuffle(cards)

    return render(request, 'cards/cards.html', {
        'cards': cards,
    })

    # print(request.GET.get('id'))
    # cards = Card.objects.filter(available_from__lte = datetime.datetime.now())

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

# @login_required
# def create_calendar(request):
    

@login_required
def edit_calendar(request, calendar_id=None):
    # the '0' here is a workaround, I don't know how to allow just cards:edit_calendar
    if calendar_id is None or calendar_id == 0:
        print("create calendar")
        if request.method == 'POST':
            form = CalendarForm(request.POST)

            if form.is_valid():
                calendar = form.save(commit=False)
                calendar.created_by = request.user
                calendar.save()

                print("saving new clendar")

                return redirect('/dashboard/')
        else:
            form = CalendarForm()

        return render(request, 'cards/calendar.html', {
            'form': form,
        })
    else:
        print("edit calendar")
        calendar = Calendar.objects.get(id = calendar_id)
        form = CalendarForm(instance=calendar)
        if request.method == 'POST':
            form = CalendarForm(request.POST, instance=calendar)
            if form.is_valid():
                calendar = form.save(commit=False)
                calendar.save()

                print("saving updated clendar")

                return redirect('/dashboard/')
        else:
            print(request.method)
            
        return render(request, 'cards/calendar.html', {
            'form': form,
            'calendar': calendar,
            # 'calendar_id': 123
        })
    
@login_required
def delete_calendar(request, calendar_id=None):
    print("delete calendar")
    calendar = Calendar.objects.get(id = calendar_id)
    calendar.delete()

    return redirect('/dashboard/')