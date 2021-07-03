from rest_framework import serializers

from polls.models import Answer
from polls.serializers.question import QuestionShortSerializer, AnswerChoiceSerializer


class AnswerCreateSerializer(serializers.ModelSerializer):
    question = QuestionShortSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = (
            'id',
            'question',
            'text',
            'choices',
            'type',
        )

    def create(self, validated_data):
        validated_data['question'] = self.context['question']
        validated_data['created_by'] = None
        validated_data['type'] = self.context['question'].type
        instance = super().create(validated_data)
        return instance


class AnswerListSerializer(serializers.ModelSerializer):
    question = QuestionShortSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = (
            'id',
            'created_by',
            'question',
            'type',
        )


class AnswerRetrieveSerializer(AnswerListSerializer):
    choices = AnswerChoiceSerializer(read_only=True, many=True)

    class Meta(AnswerListSerializer.Meta):
        fields = AnswerListSerializer.Meta.fields + (
            'text',
            'choices'
        )
