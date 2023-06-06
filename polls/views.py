from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Página inicial")

def detail(request, question_id):
    return HttpResponse(f"Essa é a pergunta de número {question_id}")

def results(request, question_id):
     return HttpResponse (f"Resultados da pergunta de número {question_id}")

def vote(request, question_id):
    return HttpResponse(f"Você vai votar na pergunta de numero {question_id}")



