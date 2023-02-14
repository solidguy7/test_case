from rest_framework import serializers
from tickets.models import Ticket

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['sender', 'subject', 'slug', 'description', 'answer', 'status', 'created']
