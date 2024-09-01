from django.shortcuts import render, redirect
from funcionarios.models import Funcionario
from django.http import Http404
from django.db.models import Q
from django.core.paginator import Paginator



def index(request):
    funcionarios = Funcionario.objects \
    .order_by('-id')

    paginator = Paginator(funcionarios, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'site_title': 'MedFutura - Funcionários',
    }

    return render(
        request,
        'funcionarios/index.html',
        context
    )

def funcionariouni(request, funcionariouni_id):
    unidade_func = Funcionario.objects.filter(pk=funcionariouni_id).first()

    if unidade_func is None:
        raise Http404()

    context = {
        'funcionario': unidade_func,
    }

    return render(
        request,
        'funcionarios/funcionariouni.html',
        context
    )

def pesquisa(request):
    valor_pesquisa = request.GET.get('q', '').strip()

    if valor_pesquisa == '':
        return redirect('funcionarios:index')

    funcionarios = Funcionario.objects \
        .order_by('-id')\
        .filter(Q(nome_Completo__icontains=valor_pesquisa) |
                Q(apelido__icontains=valor_pesquisa) |
                Q(stacks__icontains=valor_pesquisa))\
    
    paginator = Paginator(funcionarios, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)


    context = {
        'page_obj': page_obj,
        'site_title': 'Pesquisa - ',
        'valor_pesquisa': valor_pesquisa,
    }

    return render(
        request,
        'funcionarios/index.html',
        context
    )
