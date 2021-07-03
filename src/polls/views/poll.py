from django.utils import timezone

from rest_framework import viewsets

from polls.models import Poll
from polls.serializers import (
    PollShortSerializer,
    PollCreateSerializer,
    PollUpdateSerializer,
    PollRetrieveSerializer,
)


class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()

    def get_serializer_class(self):
        serializer_class = PollShortSerializer

        if self.action == 'create':
            serializer_class = PollCreateSerializer
        elif self.action in ['update', 'partial_update']:
            serializer_class = PollUpdateSerializer
        elif self.action == 'retrieve':
            serializer_class = PollRetrieveSerializer

        return serializer_class

    def get_queryset(self):
        # TODO: check it out
        now = timezone.now().astimezone().date()
        qs = self.queryset

        if self.action == 'list':
            qs = qs.filter(date_end__gte=now).only('id', 'name')
        elif self.action == 'retrieve':
            qs = qs.prefetch_related('questions')

        return qs
