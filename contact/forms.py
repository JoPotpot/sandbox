from django import forms

class ContactForm(forms.Form):
	sujet 		= forms.CharField(max_length=200)
	message 	= forms.CharField(widget=forms.Textarea)
	envoyeur 	= forms.EmailField(label='Votre adresse email')
	renvoi		= forms.BooleanField(help_text='Cochez si vous souhaitez une copie du mail envoyé', required=False)
	date_test	= forms.DateField(widget=forms.DateInput);
	