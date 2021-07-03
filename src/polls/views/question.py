from django.contrib.auth.models import AnonymousUser

from rest_framework import viewsets, mixins
from rest_framework.decorators import action
from rest_framework.response import Response

from polls.models import Question
from polls.serializers import (
    QuestionSerializer,
    QuestionCreateUpdateSerializer,
    AnswerCreateSerializer
)


class QuestionViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.RetrieveModelMixin,
                      viewsets.GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    parent_lookup = 'poll_pk'

    def get_queryset(self):
        poll_pk = self.kwargs.get(self.parent_lookup, None)
        qs = self.queryset

        if self.action == 'list':
            qs = qs.only('id', 'text', 'type').filter(poll_id=poll_pk)

        return qs

    def get_serializer_class(self):
        serializer_class = self.serializer_class

        if self.action == 'retrieve':
            serializer_class = QuestionCreateUpdateSerializer
        elif self.action == 'answer':
            serializer_class = AnswerCreateSerializer

        return serializer_class

    @action(methods=['POST'], detail=True, url_path='answer')
    def answer(self, request, *args, **kwargs):
        created_by = self.request.user
        if isinstance(created_by, AnonymousUser):
            created_by = None

        instance = self.get_object()
        serializer: AnswerCreateSerializer = self.get_serializer(
            data=self.request.data, context={
                'question': instance,
                'created_by': created_by
            }
        )
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data)
