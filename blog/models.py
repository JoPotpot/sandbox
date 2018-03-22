# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.utils import timezone

# Create your models here.
class Categorie(models.Model):
	nom = models.CharField(max_length=100)
	
	def __str__(self):
		return self.nom
		

class Article(models.Model):
	titre = 	models.CharField(max_length=100)
	slug=		models.SlugField(max_length=100)
	auteur = 	models.CharField(max_length=50)
	contenu = 	models.TextField(null=True) # null=true : peut être vide, donc champ optionnel.
	date = 		models.DateTimeField(default=timezone.now, verbose_name="Date de parution")
	categorie = models.ForeignKey('Categorie',on_delete=models.CASCADE, default=1)
	
	class Meta:
		verbose_name = 'article'
		ordering = ['date']
		
	def __str__(self):
		"""Pour mieux reconnaitre des objets pour Admin"""
		return self.titre
		
class Fiche_Contact(models.Model):
	nom		=	models.CharField(max_length=50)
	adresse	=	models.CharField(max_length=200)
	photo	=	models.ImageField(upload_to='photos/')
	
	def __str__(self):
		return self.nom