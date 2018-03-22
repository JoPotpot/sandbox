from django import forms
from .models import MiniUrl

class MiniUrlForm(forms.ModelForm):
	class Meta:
		model=MiniUrl
		fields=('URL_longue','createur')