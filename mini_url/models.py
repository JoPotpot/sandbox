from django.db import models
from django.utils import timezone
import random,string


# Create your models here.
class MiniUrl(models.Model):
	URL_longue	= models.URLField(unique=True)
	code		= models.CharField(max_length=100, unique=True)
	date		= models.DateTimeField(default=timezone.now)
	createur	= models.CharField(max_length=40, null=True)
	count		= models.IntegerField(default=0)

	def __str__(self):
		return self.code
	
	def generer(self, nb_caracteres):
		caracteres = string.ascii_letters + string.digits
		aleatoire = [random.choice(caracteres) for _ in range(nb_caracteres)]
		return 'localhost:8000/m/'.join(aleatoire)
		
	def save(self,*args,**kwargs):
		if self.pk is None:
			self.generer(10)
		super(MiniUrl,self).save(*args,**kwargs)
	
	
	class Meta:
		verbose_name='mini URL'
		verbose_name_plural='minis URLs'
		ordering = ['date',]