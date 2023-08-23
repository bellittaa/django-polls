from django.urls import path

from polls.models import Question
from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    path('cadastrar', views.QuestionCreateView.as_view(),name="question-create")


]

