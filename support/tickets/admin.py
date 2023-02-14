from django.contrib import admin
from .models import Ticket

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['sender', 'subject', 'status', 'created']
    list_filter = ['sender', 'slug', 'status', 'created']
    search_fields = ['sender', 'subject']
    prepopulated_fields = {'slug': ('subject',)}
    raw_id_fields = ['sender']
    date_hierarchy = 'created'
    ordering = ['status', 'created']
