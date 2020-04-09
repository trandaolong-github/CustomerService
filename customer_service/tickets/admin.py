from django.contrib import admin
from tickets.models import Ticket, Category


class TicketAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Ticket, TicketAdmin)
admin.site.register(Category, CategoryAdmin)
