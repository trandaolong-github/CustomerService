from django.urls import path
from . import views

urlpatterns = [
    path("", views.ticket_index, name="ticket_index"),
    path("<int:pk>/", views.ticket_detail, name="ticket_detail"),
    path("<category>/", views.ticket_category, name="ticket_category"),
]