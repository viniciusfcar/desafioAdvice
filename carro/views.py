from django.shortcuts import render, redirect, get_object_or_404
from .models import Carro
from proprietario.models import Proprietario
from .forms import FormCarro

from django.contrib.auth.decorators import login_required

@login_required(login_url='/')
def cadastro_carro(request, id):
    proprietario = get_object_or_404(Proprietario, pk=id)
    form = FormCarro(request.POST or None)

    context = {
        'form': form,
        'proprietario': proprietario
    }

    if request.method == 'POST':
        form = FormCarro(request.POST or None)

        if request.POST.get('modelo') != "" and request.POST.get('cor') != "":
            if proprietario.totalCarros < 3:
                
                carro = form.save()
                carro.proprietario = proprietario
                carro.save()
                
                if proprietario.potencialComprador:
                    proprietario.potencialComprador = False

                proprietario.totalCarros += 1
                proprietario.save()
                return redirect('listaProprietarios')
            else:
                context['msg'] = 'Este proprietário já possue 3 carros!'
                return render(request, 'cadastro_carro.html', {'context': context})

    return render(request, 'cadastro_carro.html', {'context': context})

@login_required(login_url='/')
def lista_carros(request):
    carros = Carro.objects.all()
    
    context = {
        'carros': carros
    }

    return render(request, 'lista_carros.html', {'context': context})

@login_required(login_url='/')
def delete_carro(request, id):
    carro = get_object_or_404(Carro, pk=id)

    context = {
        'carro': carro,
    }

    if request.method == 'POST':
        carro.proprietario.totalCarros -= 1
        
        if carro.proprietario.totalCarros == 0:
            carro.proprietario.potencialComprador = True
        
        carro.proprietario.save()
        carro.delete()

        return render(request, 'index.html')
    
    return render(request, 'delete_carro.html', {'context': context})
