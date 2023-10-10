from email import message
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Question
from django.forms.models import BaseModelForm 


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    response = f'Resultados da pergunta de número {question_id}'
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("Você está votando em uma enquete %s." % question_id)

from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy

class QuestionCreateView(CreateView):
    model = Question
    fields = ('question_text',)
    success_url = reverse_lazy('index')
    template_name = 'polls/question_form.html'

class QuestionListView(ListView):
   model = Question 
   context_object_name = 'questions'

class QuestionDetailView(DetailView):
    model = Question 
    context_object_name = 'question'    

class QuestionDeleteView(DeleteView):
    model =  Question 
    success_url = reverse_lazy("question_list")
    success_message = "Enquete excluída com sucesso."

    def form_valid(self, form):
        message.success(self.request, self.success_message)
        return super(). form_valid(form) 

class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-pub_date']
    paginate_by = 5

@login_required
def sobre(request):
    return HttpResponse('Este é um app de enquete!')



class QuestionUpdateView(UpdateView):
    model = Question
    success_url = reverse_lazy('question-list')
    fiels = ('question_text',)
    success_url = reverse_lazy('plls_all')
    success_message = 'Pergunta atualizada com sucesso!'

    def get_context_data(self, **kwargs):
        conext = super(QuestionUpdateView, self). def get_context_data(self, **kwargs)
        context['form_title'] = 'Editando a pergunta'

        question_id = self.kwargs.get('pk')
        choices = choice.objects.filter(question__pk=question_id)
        context['question_choices'] = choices

        return context


    def form_valid(self, request, *args, **kwargs):
        messages.success(self, request, self.success_message)
        return super(QuestionUpdateView,self).def form_valid(request, *args, **kwargs)
         
    
   