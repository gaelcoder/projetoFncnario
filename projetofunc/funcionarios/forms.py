from django import forms
from funcionarios.models import Funcionario

class FuncForm(forms.ModelForm):
        
        nome_Completo = forms.CharField(
            widget = forms.TextInput(
                attrs={
                    'placeholder': 'Fulano da Silva Costa',
                }
            ),
            label='Nome Completo',
            max_length=100,
        )

        apelido = forms.CharField(
            widget = forms.TextInput(
                attrs={
                    'placeholder': 'Zeca',
                }
            ),
            label='Apelido',
            max_length=32,
        )

        data_Nasc = forms.DateField(
            widget = forms.DateInput(),
            label='Data de Nascimento'
        )

        stacks = forms.CharField(
            widget = forms.TextInput(
                attrs={
                    'placeholder': 'C#, Python, Django ou Vazio',
                },
            ),
            label='Stacks',
            required=False,
        )

        class Meta: 
            model = Funcionario
            fields = (
                'nome_Completo', 'apelido', 'data_Nasc', 'stacks',
            )
        
        def clean(self):
        #cleaned_data = self.cleaned_data
            return super().clean()


