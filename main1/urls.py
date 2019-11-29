from django.urls import path
from main import views
app_name = 'main'

urlpatterns = [
    path('event/', views.event, name='event'),
    path('events/', views.events, name='create_event'),
    path('ticket/', views.ticket, name='ticket'),
    path('tickets/', views.tickets, name='tickets')
]