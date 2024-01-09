from django.urls import path

from . import views

app_name = 'cards'

urlpatterns = [
    # ex: /cards/
    path('', views.index, name='index'),
    # ex: /cards/5/
    path('<int:calendar_id>/', views.cards, name="cards"),
    path('calendar/', views.edit_calendar, name='create_calendar'),
    path('calendar/<int:calendar_id>/', views.edit_calendar, name='edit_calendar'),
    path('calendar/<int:calendar_id>/delete/', views.delete_calendar, name='delete_calendar'),
    path('<int:pk>/create-card/', views.create_card, name='create_card'),
    path('htmx/create-card-form/', views.create_card_form, name='create-card-form'),
    path('htmx/card/<pk>/', views.detail_card, name='detail-card'),
    path('htmx/card/<pk>/delete/', views.delete_card, name='delete-card'),
    path('htmx/card/<pk>/update/', views.update_card, name='update-card'),
]