from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from polls.views import PollViewSet, QuestionViewSet, AnswerViewSet


router = DefaultRouter()
router.register(r'polls', PollViewSet, basename='poll')
router.register(r'answers', AnswerViewSet, basename='answer')


questions_router = routers.NestedDefaultRouter(router, r'polls', lookup='poll')
questions_router.register('questions', QuestionViewSet, basename='question')

answers_router = routers.NestedDefaultRouter(questions_router, r'questions', lookup='question')
answers_router.register('answers', AnswerViewSet, basename='question_answers')

urlpatterns = [] + router.urls + questions_router.urls + answers_router.urls
