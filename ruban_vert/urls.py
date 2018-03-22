from django.urls import path
from . import views

urlpatterns = [
	path('enreg', views.form_enreg, name='enregistrement'),
	path('enreg/<id>', views.modif_enreg, name='modifier enreg'),
	path('list_enreg', views.list_enreg, name='liste enreg'),
	]