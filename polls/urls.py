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
    path('<int:pk>', views.QuestionDetailView.as_view(), name="question-detail")

    

]

