from rest_framework import viewsets, mixins

from polls.models import Answer
from polls.serializers import AnswerListSerializer, AnswerRetrieveSerializer


class AnswerViewSet(mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerListSerializer
    lookup_parent = 'question_pk'

    def get_queryset(self):
        question_pk = self.kwargs.get(self.lookup_parent, None)
        qs = self.queryset

        if self.action == 'list':
            qs = qs.only('id', 'created_by', 'question', 'type').select_related('created_by', 'question')
            if question_pk:
                qs = qs.filter(question_id=question_pk)

        return qs

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'retrieve':
            serializer_class = AnswerRetrieveSerializer

        return serializer_class
