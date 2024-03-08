from django.shortcuts import render

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
        
        usuarios = {
            'usuarios': Usuario.objects.all(),
            'message': message
        }
        return render(request, 'sua_template.html', usuarios)
    else:
        # Certifique-se de retornar um HttpResponse em todos os casos possíveis.
        # Aqui, estamos retornando uma página vazia se o método não for POST.
        return HttpResponse()
