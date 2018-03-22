from django.urls import path, re_path
from . import views

urlpatterns = [
	path('accueil', views.accueil_blog, name='accueil du blog'),
	path('article/<int:id>-<slug:slug>', views.lire, name='lire un article'),
	path('form', views.formulaire_article, name='nouvel article'),
	#partie fichiers photos dans contacts
	path('fiche_contact', views.nouvelle_fiche_contact, name='fiche contact'),
	path('voir_contacts', views.voir_contacts, name='voir contacts'),
	]