# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from blog.models import Article,Categorie
from django.utils.text import Truncator


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('titre', )}
	#Infos sur la liste et criteres de recherche
	list_display	=('titre', 'auteur', 'apercu_contenu','date')
	list_filter		=('auteur','categorie')
	date_hierarchy	='date'
	ordering		=('date',)
	search_fields 	=('titre', 'contenu')
	
	#regroupement de champs a ledition
	fieldsets = (
	# premier fieldset avec les metainfos
		('Général', {
			'classes':['collapse',],
			'fields': ('titre', 'slug', 'auteur', 'categorie')
		}),
		# second fieldset avec le contenu
		('Contenu de l\'article', {
		'description':'Le formulaire accepte les balises HTML.',
		'fields': ('contenu',)
		}),
	)

	
	#colonne speciale resume
	def apercu_contenu(self, article):
		return Truncator(article.contenu).chars(40,truncate='...')
	apercu_contenu.short_description='Debut de l\'article'
	
admin.site.register(Article, ArticleAdmin)
admin.site.register(Categorie)


