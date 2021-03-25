from django.shortcuts import render, redirect
from django.http import HttpResponse
from quiz.base.models import Pergunta
from quiz.base.forms import AlunoForm

# Create your views here.


def home(request):
    if request.method == 'POST':
        formulario = AlunoForm(request.POST)
        if formulario.is_valid():
            aluno = formulario.save()
            return redirect('/perguntas/1')
        else:
            contexto = {'formulario': formulario}
            return  render(request, 'base/home.html', contexto)
    return  render(request, 'base/home.html')


def perguntas(request, indice):
    pergunta = Pergunta.objects.filter(disponivel=True).order_by('id')[indice - 1]
    contexto = {'indice_da_questao': indice, 'pergunta': pergunta}
    return  render(request, 'base/game.html', context=contexto)


def classificacao(request):
    return render(request, 'base/classificacao.html')