from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Document
from .forms import DocumentForm, LoginForm

from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required



# Create your views here.

def main(request):
    form = DocumentForm()

    # Carregar documentos para uma lista

    documents = Document.objects.all()

    materias = Document.objects.values_list('materia', flat=True).distinct()

    
    

    context = {
        'documents': documents[::-1],
        'form': form,
        'materias' : materias
        
    }

    return render(request, 'index.html', context)

@login_required
def upload(request):

    message = ''

    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        

        if form.is_valid():

            name = form.cleaned_data['name']
            materia = form.cleaned_data['materia']

            materia = materia.replace(" ","")
            materia = materia.upper()

            newdoc = Document(docfile = request.FILES['docfile'], name = name, materia= materia)
            
            newdoc.save()
                    

            message = 'Arquivo enviado !!'
            

            return redirect('menu')

        else:
            message = 'Ops... algo deu errado'
    else:
        form = DocumentForm()

    # Carregar documentos para uma lista

    documents = Document.objects.all()
    

    context = {
        'documents': documents,
        'form': form,
        'message': message
        
    }

    return render(request, 'files.html', context)


def login(request):

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():


            username = request.POST['username']
            password = request.POST['password']

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('menu')
            else:
                return HttpResponse("Algo deu errado")

    else:

        form = LoginForm()

        context = {
            'form' : form
        }

        return render(request, 'login.html', context)


def logout_page(request):
    logout(request)
    return redirect('menu')


def materia_page(request, id=id):

    documents  = Document.objects.filter(materia=id)

    if documents:

        context = {
            'documents' : documents,
            'materia': id
        }

        return render(request, 'materia.html', context)

    else:
        return render(request, 'erro.html')




      