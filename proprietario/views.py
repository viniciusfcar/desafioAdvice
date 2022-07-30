from django.shortcuts import render, redirect, get_object_or_404
from .models import Proprietario
from carro.forms import FormCarro

from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def cadastro_proprietario(request):
    form = FormCarro(request.POST or None)
    context = {
        'form': form
    }

    if request.method == 'POST':
        
        form = FormCarro(request.POST or None)

        if request.POST.get('modelo') != "" and request.POST.get('cor') != "":
            proprietario = Proprietario(nome=request.POST.get('nome'), potencialComprador=False, totalCarros=1)
            proprietario.save()
            
            carro = form.save()
            carro.proprietario = proprietario
            carro.save()
        else:
            proprietario = Proprietario(nome=request.POST.get('nome'), potencialComprador=True, totalCarros=0)
            proprietario.save()

        return redirect('listaProprietarios')
        
    return render(request, 'cadastro_proprietario.html', {'context': context})

@login_required(login_url='/')
def lista_proprietarios(request):
    proprietarios = Proprietario.objects.all()
    form = FormCarro()

    context = {
        'proprietarios': proprietarios,
        'form': form
    }

    return render(request, 'lista_proprietarios.html', {'context': context})

@login_required(login_url='/')
def delete_proprietario(request, id):
    proprietario = get_object_or_404(Proprietario, pk=id)

    context = {
        'proprietario': proprietario,
    }

    if request.method == 'POST':
        proprietario.delete()

        return render(request, 'index.html')
    
    return render(request, 'delete_proprietario.html', {'context': context})

@login_required(login_url='/')
def alterar_proprietario(request, id):
    proprietario = get_object_or_404(Proprietario, pk=id)

    context = {
        'proprietario': proprietario,
    }

    if request.method == 'POST':
        proprietario.nome = request.POST.get('nome')
        proprietario.save()

        return redirect('listaProprietarios')
    
    return render(request, 'alterar_proprietario.html', {'context': context})
