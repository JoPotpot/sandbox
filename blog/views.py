# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from blog.models import Article, Fiche_Contact
from .forms import ArticleForm, Fiche_ContactForm


# Create your views here.	
def view_article(request, numero):
	"""requete d'une vue d'article via son numéro"""
	if int(numero) < 0:
		raise Http404
	elif numero > 99:
		numero = numero % 100
		return redirect('article', numero=numero)

	
	return HttpResponse("<h1>Article numéro #{0} </h1>".format(numero) )
	
def view_list_articles_by_date(request, year, month=1):
	return render(request, 'blog/archives.html', locals() )

def date_actuelle(request):
	return render(request, 'blog/date.html', {'date': datetime.now() } )
	
def addition(request, terme1, terme2):
	total = terme1+terme2
	return render(request, 'blog/addition.html', locals() )
	
def accueil_blog(request):
	articles=Article.objects.all()
	return render(request, 'blog/accueil.html', {'derniers_articles': articles } )

def lire(request, id, slug):
	article =get_object_or_404(Article, id=id, slug=slug)
	return render(request, 'blog/article.html', {'article' : article} )

def formulaire_article(request):
	form=ArticleForm(request.POST or None)
	if form.is_valid():
		form.save()
	return render(request, 'blog/nouvel_art.html', locals() )

def modifier_article(request, article):
	form=ArticleForm(request.POST, instance=article)
	return render(request, 'blog/nouvel_art.html', locals() )
	

#Module de fiches contacts, avec photos
def nouvelle_fiche_contact(request):
	sauvegarde=False
	form=Fiche_ContactForm(request.POST or None, request.FILES)
	if form.is_valid():
		form.save()
		sauvegarde=True
	return render(request, 'blog/nouvelle_fiche.html', locals() )

def voir_contacts(request):
	return render(request, 'blog/voir_contact.html',\
	{'contacts':Fiche_Contact.objects.all()})
	