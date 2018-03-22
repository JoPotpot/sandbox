from django.shortcuts import render
from .models import MiniUrl
from .forms import MiniUrlForm

# Create your views here.
def list_redirections(request):
	return render(request, 'mini_url/liste.html', {'Urls': MiniUrl.objects.all()})
	
	
	
	
def form_redirection(request):
	form=MiniUrlForm(request.POST or None)
	if form.is_valid():
		form.code='localhost:8000/uihhuuih'
		envoi=True
		form.save()
	return render(request, 'mini_url/form.html', locals())
	
def redirection(request,id):
	instance=MiniUrl.objects.get(id=id)
	instance.count+=1
	return render(request, instance.URL_longue, locals())