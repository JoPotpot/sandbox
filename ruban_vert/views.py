from django.shortcuts import render

from .forms import EnregForm
from .models import Enregistrement_Caisse


# Create your views here.
def list_enreg(request):
	enregs=Enregistrement_Caisse.objects.all()
	return render(request, 'ruban_vert/liste_enreg.html', {'enregistrements' : enregs}  )

def form_enreg(request):
	form=EnregForm(request.POST or None)
	if form.is_valid():
		form.save()
		envoi=True
	return render(request, 'ruban_vert/enregistrement.html', locals() )

def modif_enreg(request, id):
	form=EnregForm(instance=Enregistrement_Caisse.objects.get(id=id))
	return render(request, 'ruban_vert/enregistrement.html', locals() )

