from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import (
    authenticate,
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            
            if user is None:
                msg_error = 'Usuário inválido'
                return render(request, 'login.html', {'msg': msg_error})
            else:

                if not user.check_password(password):
                    msg_error = 'Senha inválida'
                    return render(request, 'login.html', {'msg': msg_error})
                else:
                    user = authenticate(username=username, password=password)
                    auth_login(request, user)
                        
                    return redirect('index')

        except Exception:
            msg_error = 'Usuário e/ou Senha inválido(s)'
            return render(request, 'login.html', {'msg': msg_error})

    return render(request, 'login.html')

def logout(request):
    auth_logout(request)
    return redirect('/')
