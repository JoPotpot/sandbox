from django.urls import path
from . import views

urlpatterns = [
	path('liste', views.list_redirections, name='liste mini_url'),
	path('form', views.form_redirection, name='form MiniUrl'),
	]