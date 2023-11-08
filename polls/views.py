from email import message
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Choice, Question
from django.forms.models import BaseModelForm 
from django.contrib import messages


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

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ('question_text',)
    success_url = reverse_lazy('index')
    template_name = 'polls/question_form.html'
    success_message = 'Pergunta criada com sucesso!'

    def get_context_data(self, **kwargs):
        context = super(QuestionCreateView, self).get_context_data  (**kwargs)
        context['form_title'] = 'Criando uma pergunta'

        return context

    def form_valid(self,form):
        form.instance.author = self.request.user
        messages.succes(self.request, self.success_message)
        return super(QuestionCreateView, self). form_valid(form)

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
        context = super(QuestionUpdateView, self).get_context_data(self, **kwargs)
        context['form_title'] = 'Editando a pergunta'

        question_id = self.kwargs.get('pk')
        choices = Choice.objects.filter (question__pk=question_id)
        context['question_choices'] = choices

        return context


    def form_valid(self, request, *args, **kwargs):
        message.success(self, request, self.success_message)
        return super(QuestionUpdateView,self).form_valid(request, *args, **kwargs)
         
    
class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'polls/question_confirm_delete_form.html'
    success_url = reverse_lazy('polls_all')
    success_message = 'Pergunta excluída com sucesso!'

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(QuestionDeleteView, self).form_valid(request, *args, **kwargs)

class QuestionDetailView(DetailView):
    model = Question
    template_name = 'polls/question_detail.html'
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        question_id = self.kwargs.get('pk')
        choices = Choice.objects.filter(question__pk=question_id)
        context['question_choices'] = choices

        return context

class QuestionListView(ListView):
    model = Question
    template_name = 'polls/question_list.html'
    context_object_name = 'questions'
    paginate_by = 3
    ordering = ['-pub_date']


class ChoiceCreateView(CreateView):
    model = Choice
    template_name = 'polls/choice_form.html'
    fields = ('choice_text', )
    success_message = 'Pergunta criada com sucesso!'

    def dispatch(self, request, *args, **kwargs):
        self.question = get_object_or_404(Question, pk=self.kwargs.get('pk'))
        return super(ChoiceCreateView, self).dispatch(request,  *args, **kwargs)

    def get_context_data(self, **kwargs):
        # question = get_object_or_404(Question,  pk=self.kwargs.get('pk'))
        context = super(ChoiceCreateView, self).get_context_data(**kwargs)
        context['form_title'] = f'Alternativa para:{self.question.question_text}'

        return context

    def form_valid(self, form):
        form.instance.question = self.question
        messages.success(self.request, self.success_message)
        return super(ChoiceCreateView, self).form_valid(form)
    
    def get_success_url(self, *args, **kwargs):
        question_id = self.kwargs.get('pk')
        return reverse_lazy('poll_edit', kwargs={'pk': question_id})


class ChoiceUpdateView(UpdateView):
    model = Choice
    template_name = 'polls/choice_form.html'
    fields = ('choice_text', )
    success_message = 'Alternativa atualizada com sucesso!'

    def get_context_data(self, **kwargs):
        context = super(ChoiceUpdateView, self).get_context_data(**kwargs)
        context['form_title'] = 'Editando alternativa'

        return context

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ChoiceUpdateView, self).form_valid(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        question_id = self.object.question.id
        return reverse_lazy('poll_edit', kwargs={'pk': question_id})

class ChoiceDeleteView(LoginRequiredMixin, DeleteView):
    model = Choice
    template_name = 'polls/choice_confirm_delete_form.html'
    success_message = 'Alternativa excluída com sucesso!'

    def form_valid(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(ChoiceDeleteView, self).form_valid(request, *args, **kwargs)

    def get_success_url(self, *args, **kwargs):
        question_id = self.object.question.id
        print(question_id)
        return reverse_lazy('poll_edit', kwargs={'pk': question_id})