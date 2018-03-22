from django import forms
from .models import Enregistrement_Caisse, Registre_Tarif_Loc

class EnregForm(forms.ModelForm):
	class Meta:
		model=Enregistrement_Caisse
		#fields='nom','prenom','type_loc','duree_loc'
		fields='__all__'
		
	# def donne_prix(self):
		
		# tarif = Registre_Tarif_Loc.objects.get(duree_loc=self.duree_loc, \
										# type_loc =self.type_loc)
		# prix = tarif.prix								
			
	def clean(self):
		duree=self.cleaned_data['duree_loc']
		type=self.cleaned_data['type_loc']
		
		tarif = Registre_Tarif_Loc.objects.get(duree_loc=duree, \
										type_loc =type)		
		self.cleaned_data['prix']=tarif.prix
		return self.cleaned_data

			
		
# nom 			= models.CharField(max_length=80)
# prenom 		= models.CharField(max_length=80)
# commentaire	= models.TextField(null=True)
# date_loc		= models.DateTimeField(default=timezone.now, verbose_name="Date de location")
# tarif			= models.ForeignKey('Registre_Tarif_Loc',on_delete=models.SET_NULL, null=True, default=1)
# prix 			= models.DecimalField(max_digits=6, decimal_places=2)
# duree_loc		= models.ForeignKey('Duree_Loc',on_delete=models.SET_NULL, null=True, default=1)
# type_loc		= models.ForeignKey('Type_Loc',on_delete=models.SET_NULL, null=True, default=1)
