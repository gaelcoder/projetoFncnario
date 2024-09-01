from django.shortcuts import render, redirect
from pathlib import Path
import json
from funcionarios.forms import FuncForm

CAMINHO_ATUAL = Path(__file__).parent / 'dadosfuncionarios.json'

def create(request):

    if request.method == 'POST':

        form = FuncForm(request.POST)
        context = {
            'form': form,
        }

        if form.is_valid():
            form.save()
            with open(CAMINHO_ATUAL, 'a') as arquivo:
                json.dump(request.POST, arquivo, ensure_ascii=True, indent=4)
            arquivo.close()
            return redirect('funcionarios:create')
        

        return render(
            request,
            'funcionarios/create.html',
            context
        )
    
    context = {
        'form': FuncForm()
    }

    return render(
        request,
        'funcionarios/create.html',
        context
    )