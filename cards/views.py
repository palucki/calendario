import random

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse, Http404

from .forms import CalendarForm, CardForm, CardFormSet
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
def create_card(request, pk):
    """
    pk - ID of the calendar
    """
    calendar = Calendar.objects.get(pk=pk)
    cards = Card.objects.filter(calendar=calendar)
    form = CardForm(request.POST or None)
   
    print("CreateCard")

    if request.method == 'POST':
        if form.is_valid():
            card = form.save(commit=False)
            card.calendar_id = pk
            card.created_by = request.user
            card.ordering = 1
            card.save()
            # formset.instance = calendar
            # new_card = formset.save(commit=False)
            # for nc in new_card:
            #     nc.created_by = request.user
            #     # TODO: clean this up
            #     nc.ordering = 1 
            # formset.save()

            # return redirect('/cards/htmx/card/{}/'.format(calendar.id))
            return redirect('/cards/htmx/card/{}/'.format(card.id))
        else:
            return render(request, 'cards/create_card_component.html', {
                "form": form
            })
    #     form = CardForm(request.POST)

    #     if form.is_valid():
    #         card = form.save(commit=False)
    #         card.created_by = request.user
    #         card.save()

    #         return redirect('/dashboard/')
    # else:
    #     form = CardForm()
    #     form.fields['calendar'].queryset = Calendar.objects.filter(created_by=request.user)

    return render(request, 'cards/create_card.html', {
        "form" : form,
        "calendar" : calendar,
        "cards": cards
    })

@login_required
def create_card_form(request):
    return render(request, 'cards/create_card_component.html', {
        "form": CardForm()
    })

@login_required
def detail_card(request, pk):
    card = Card.objects.get(pk=pk)
    return render(request, 'cards/card_detail_component.html', {
        "card": card
    })

@login_required
def delete_card(request, pk):
    card = Card.objects.get(pk=pk)
    card.delete()
    return HttpResponse('')

@login_required
def update_card(request, pk):
    card = Card.objects.get(pk=pk)
    form = CardForm(request.POST or None, instance=card)

    print("UpdateCard")

    if request.method == 'POST':
        card_text = request.POST.get('text', '')
        print("CARD TEXT:")
        print(card_text)
        if form.is_valid():
            card = form.save(commit=False)

            # TODO: hardcoded claendar id and ordering!!!
            card.calendar_id = 1
            card.created_by = request.user
            card.ordering = 1
            card.save()
            return redirect('/cards/htmx/card/{}/'.format(card.id))

    return render(request, 'cards/create_card_component.html', {
        "form": form,
        "card": card
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