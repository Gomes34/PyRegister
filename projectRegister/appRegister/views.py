from django.shortcuts import render
from django.http import HttpResponse
from .models import Usuario

def home(request):
    return render(request, 'usuarios/home.html')

def usuarios(request):
    if request.method == 'POST':
        novoUsuario = Usuario()
        novoUsuario.nome_usuario = request.POST.get('nomeUsuario')
        novoUsuario.email_usuario = request.POST.get('emailUsuario')
        
        if Usuario.objects.filter(email_usuario=novoUsuario.email_usuario).exists():
            message = "O valor já existe no banco de dados."
        else:
            novoUsuario.save()
            message = "Usuário criado com sucesso!"
        
    else:
        message = ""

    usuarios = {
        'usuarios': Usuario.objects.all(),
        'message': message
    }
    return render(request, 'usuarios/usuarios.html', usuarios)
