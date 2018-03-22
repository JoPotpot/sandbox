from django.contrib import admin
from ruban_vert.models import 	Duree_Loc, Type_Loc, \
								Enregistrement_Caisse, \
								Registre_Tarif_Loc
from django.utils.text import Truncator

# Register your models here.
class Registre_Tarif_LocAdmin(admin.ModelAdmin):
	list_display	=('duree_loc', 'type_loc', 'prix')
	list_filter		=('duree_loc','type_loc')
	
class Enregistrement_CaisseAdmin(admin.ModelAdmin):
	list_display	=('nom_client', 'apercu_commentaire','prix')
	date_hierarchy	='date_loc'
	ordering		=('date_loc',)
	search_fields 	=('nom', 'prenom')
	
	#colonne speciale commentaire
	def apercu_commentaire(self, enreg):
		return Truncator(enreg.commentaire).chars(10,truncate='...')
	apercu_commentaire.short_description='comm.'
	
	#colonne client
	def nom_client(self, enreg):
		return '%s %s' % (enreg.nom,enreg.prenom)
	nom_client.short_description='client'

	
admin.site.register(Duree_Loc)
admin.site.register(Type_Loc)
admin.site.register(Enregistrement_Caisse,Enregistrement_CaisseAdmin)
admin.site.register(Registre_Tarif_Loc,Registre_Tarif_LocAdmin)