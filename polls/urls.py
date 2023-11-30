from django.urls import path

from polls.models import Question
from . import views
urlpatterns = [
    # function based viws
    # path("", views.index, name="index"),
    # path("<int:question_id>/", views.detail, name="detail"),
    # path("<int:question_id>/results/", views.results, name="results"),
    # path("<int:question_id>/vote/", views.vote, name="vote"),

    # class based views 
    path('listar', views.QuestionListView.as_view(),name = "question-list"),
    path('cadastrar', views.QuestionCreateView.as_view(),name="question-create"),
    path('<int:pk>', views.QuestionDetailView.as_view(), name="question-detail"),
    path('<int:pk>/deletar', views.QuestionDeleteView.as_view(), name='question-delete'),
    path('<int:pk/atualizar', views.QuestionUpdateView.as_view(), name="question-update"),
    path('pergunta/<int:pk>/alternativa/add', views.ChoiceCreateView.as_view(), name="choice add"),
    path('alternativa/cint:pka/edit', views.ChoiceUpdateView.as_view(), name="choice_edit"),
    path('alternativa/<int:pk>/delete', views.ChoiceDeleteView.as_view(), name="choice delete"),
    path('pergunta/<int:question_id>vote', views.vote, name="poll_vote"),
    path('pergunta/<int:question_id>/results', views.results, name= "poll_results")


]
