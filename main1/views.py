from django.shortcuts import render, redirect

from main.forms import EventForm, TicketForm
from .models import Event, Ticket
from django.core.files.storage import FileSystemStorage
# Create your views here.


def home(request):
    if request.user is not None and str(request.user) != 'AnonymousUser':
        # return render(request, "base.html", {"title": "home"})
        return redirect('/test/events/')
    else:
        return redirect("/logout/")


def event(request):
    if request.user is not None and str(request.user) != 'AnonymousUser':
        if request.method == "POST":
            ev = Event()
            form = EventForm(request.POST, instance=ev)

            if form.is_valid():

                form.save()
            events = Event.objects.all()
            return render(request, "events.html", {"title": "Event", "records": events})
        else:
            form = EventForm()
            return render(request, "create_event.html", {"form": form})
    else:
        return redirect("/logout/")


def events(request):
    if request.user is not None and str(request.user) != 'AnonymousUser':
        print(request.user)
        events = Event.objects.all()
        return render(request, "events.html", {"title": "Event", "records": events})
    else:
        return redirect("/logout/")


def ticket(request):
    if request.user is not None and str(request.user) != 'AnonymousUser':
        if request.method == "POST":
            # ticket_obj = Ticket()
            form = TicketForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()
            tickets = Ticket.objects.all()
            return render(request, "tickets.html", {"title": "Event", "records": tickets})
        else:
            form = TicketForm()
            return render(request, "create_ticket.html", {"form": form})
    else:
        return render(request, "logout.html")


def tickets(request):
    if request.user is not None and str(request.user) != 'AnonymousUser':
        tickets = Ticket.objects.all()
        return render(request, "tickets.html", {"title": "Event", "records": tickets})
    else:
        return redirect("/logout/")
