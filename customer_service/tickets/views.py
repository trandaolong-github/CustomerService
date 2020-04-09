from django.shortcuts import render
from tickets.models import Ticket, Comment
from .forms import CommentForm


def ticket_index(request):
    # The minus sign tells Django to start with the largest value rather than the smallest. 
    # We use this, as we want the posts to be ordered with the most recent post first.
    tickets = Ticket.objects.all().order_by('-created_on')
    context = {
        "tickets": tickets,
    }
    return render(request, "ticket_index.html", context)


def ticket_category(request, category):
    tickets = Ticket.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "tickets": tickets
    }
    return render(request, "ticket_category.html", context)


def ticket_detail(request, pk):
    ticket = Ticket.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                ticket=ticket
            )
            comment.save()

    comments = Comment.objects.filter(ticket=ticket)
    context = {
        "ticket": ticket,
        "comments": comments,
        "form": form
    }

    return render(request, "ticket_detail.html", context)