from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def contact(request):
	form=ContactForm(request.POST or None)
	if form.is_valid():

		envoi=True
		
	return render(request, 'contact/contact.html', locals() )
