import json

from rest_framework import serializers

from polls.models import Poll, Question
from polls.serializers.question import QuestionShortSerializer, QuestionCreateUpdateSerializer


class PollShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = (
            'id',
            'name'
        )


class PollCreateSerializer(PollShortSerializer):
    questions = QuestionCreateUpdateSerializer(many=True)

    class Meta(PollShortSerializer.Meta):
        fields = PollShortSerializer.Meta.fields + (
            'questions',
            'description',
            'date_start',
            'date_end',
        )

    def create(self, validated_data):
        # Very scary stupid code, i am sorry
        questions = json.loads(json.dumps(validated_data.pop('questions')))
        instance = super().create(validated_data)
        for question in questions:
            choices = question.pop('choices')
            question_obj = Question.objects.create(poll=instance, **question)
            for choice in choices:
                question_obj.choices.create(**choice)
        return instance


class PollUpdateSerializer(PollCreateSerializer):
    class Meta(PollCreateSerializer.Meta):
        fields = PollCreateSerializer.Meta.fields
        read_only_fields = ('date_start',)

    def update(self, instance, validated_data):
        questions = validated_data.pop('questions', None)
        questions_objs = json.loads(json.dumps(questions))
        instance = super().update(instance, validated_data)
        instance.questions.all().delete()
        if questions:
            for question in questions_objs:
                choices = question.pop('choices')
                question_obj = Question.objects.create(poll=instance, **question)
                for choice in choices:
                    question_obj.choices.create(**choice)
        return instance


class PollRetrieveSerializer(PollShortSerializer):
    questions = QuestionShortSerializer(many=True, read_only=True)

    class Meta(PollShortSerializer.Meta):
        fields = PollShortSerializer.Meta.fields + (
            'questions',
            'description',
            'date_start',
            'date_end',
        )
