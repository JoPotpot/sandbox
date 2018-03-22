from django import forms
from .models import Article, Fiche_Contact

class ArticleForm(forms.ModelForm):
	class Meta:
		model=Article
		fields='__all__'
		prepopulated_fields = {'slug': ('titre', )}
		# fieldsets=(
			# ("Informations",	{
				# 'fields':('titre','auteur', 'categorie')}),
			# ("Adresse", {
				# 'classes':['collapse',],
				# 'fields':('slug',)
			# }),
			# ("Contenu du billet de blog", {
				# 'fields':('contenu',)},
			# )
		# )
		
class Fiche_ContactForm(forms.ModelForm):
	class Meta:
		model=Fiche_Contact
		fields="__all__"