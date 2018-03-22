from django.db import models
from django.utils import timezone

# Create your models here.
class Duree_Loc(models.Model):
	choix		= models.CharField(max_length=80)

	def __str__(self):
		return self.choix
	
class Type_Loc(models.Model):
	bateau		= models.CharField(max_length=80)
	
	def __str__(self):
		return self.bateau
		
class Registre_Tarif_Loc(models.Model):
	duree_loc	= models.ForeignKey('Duree_Loc',on_delete=models.CASCADE, default=1)
	type_loc	= models.ForeignKey('Type_Loc',on_delete=models.CASCADE, default=1)
	prix		= models.DecimalField(max_digits=6, decimal_places=2)
	
	def __str__(self):
		return '%s %s' % (self.duree_loc, self.type_loc)
	
	
class Enregistrement_Caisse(models.Model):
	nom 		= models.CharField(max_length=80)
	prenom 		= models.CharField(max_length=80)
	commentaire	= models.TextField(null=True, blank=True)
	date_loc	= models.DateTimeField(default=timezone.now, verbose_name="Date de location")
	tarif		= models.ForeignKey('Registre_Tarif_Loc',on_delete=models.SET_NULL, null=True, default=1)
	prix 		= models.DecimalField(max_digits=6, decimal_places=2,null=True, blank=True)
	duree_loc	= models.ForeignKey('Duree_Loc',on_delete=models.SET_NULL, null=True, default=1)
	type_loc	= models.ForeignKey('Type_Loc',on_delete=models.SET_NULL, null=True, default=1)
	
	class Meta:
		verbose_name	='Enregistrement'
		ordering		=['date_loc']
	
	def __str__(self):
		return '%s %s' % (self.nom, self.prenom)