from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import TicketSerializer
from tickets.models import Ticket
from tickets.tasks import ticket_created

class TicketViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    @action(detail=True, methods=['post'], authentication_classes=[JWTAuthentication], permission_classes=[IsAuthenticated])
    def send_ticket(self, request, *args, **kwargs):
        ticket = self.get_object()
        ticket_created.delay(ticket.id)
        return Response({'sent': True})
