from django import forms

class LoginForms(forms.Form):
    nome = forms.CharField(
        label = 'Nome do usuário',
        required = True,
        max_length = 100,
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'EX.: João Silva'
            }
        )
    )

    senha = forms.CharField(
        label = 'Senha',
        required = True,
        max_length = 70,
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Digite sua senha',
            }
        )
    )

class CadastroForms(forms.Form):
    nome = forms.CharField(
        label = 'Nome',
        required = True,
        max_length= 100,
        widget= forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
             }

        )
    )

    email = forms.EmailField(
        label='Email',
        required=True,
        max_length=100,
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'EX.: João Silva'
            }
        )
    )

    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=70,
        widget= forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite sua senha'
            }
        )
    )

    confirmacao_senha=forms.CharField(
        label= 'Confirme sua senha',
        required= True,
        max_length= 70,
        widget= forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Confirme sua senha'
            }
        )
    )

    def clean_senha_confirmacao(self):
        senha_1 = self.cleaned_data.get("senha")
        senha_2 = self.cleaned_data.get("senha_confirmacao")

        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError("As senhas não são iguais.")
            else:
                return senha_2