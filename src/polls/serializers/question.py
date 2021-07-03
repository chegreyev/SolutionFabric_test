from rest_framework import serializers

from polls.models import Question, AnswerChoice


class QuestionShortSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = (
            'id',
            'text',
        )


class QuestionSerializer(QuestionShortSerializer):

    class Meta(QuestionShortSerializer.Meta):
        fields = QuestionShortSerializer.Meta.fields + ('type',)


class AnswerChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = AnswerChoice
        fields = (
            'id',
            'text'
        )


class QuestionCreateUpdateSerializer(QuestionSerializer):
    choices = AnswerChoiceSerializer(many=True, required=False, default=None)

    class Meta(QuestionSerializer.Meta):
        fields = QuestionSerializer.Meta.fields + (
            'choices',
        )

    def update(self, instance, validated_data):
        choices = validated_data.pop('choices')
        return super().update(instance, validated_data)
