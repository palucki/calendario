from django.urls import path

from . import views

app_name = 'cards'

urlpatterns = [
    # ex: /cards/
    path('', views.index, name='index'),
    # ex: /cards/5/
    path('<int:calendar_id>/', views.cards, name="cards"),
    path('calendar/', views.edit_calendar, name='create_calendar'),
    path('calendar/<int:calendar_id>', views.edit_calendar, name='edit_calendar'),
    path('calendar/<int:calendar_id>/delete/', views.delete_calendar, name='delete_calendar'),
    path('create-card/', views.create_card, name='create_card')
]