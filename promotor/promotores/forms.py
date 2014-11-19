"""from django import forms
from promotores.models import Pessoa


class PessoaForm(forms.ModelForm):
	class Meta:
		model=Pessoa

class LoginForm(forms.Form):
	login = forms.CharField(max_length =150, required =True)
	senha = forms.CharField(widget=forms.PasswordInput, required=True)
	"""