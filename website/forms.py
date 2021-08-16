from django import forms


class DocumentForm(forms.Form):
    docfile = forms.FileField(label='escolha um arquivo')
    name = forms.CharField(label='escolha um nome')
    materia = forms.CharField(label = 'matéria')

    

class LoginForm(forms.Form):
    username = forms.CharField(label='Usuário', required=True)
    password = forms.CharField(widget=forms.PasswordInput(render_value = True), label = 'Senha')