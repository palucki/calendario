from django.urls import path

from . import views

app_name = 'cards'

urlpatterns = [
    # ex: /cards/
    path('', views.index, name='index'),
    # ex: /cards/5/
    path("<int:calendar_id>/", views.cards, name="cards"),
    path('create-calendar/', views.create_calendar, name='create_calendar'),
    path('create-card/', views.create_card, name='create_card')
]