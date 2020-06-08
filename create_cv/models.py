from django.db import models
from django.contrib.auth.models import User
from phone_field import PhoneField

class Infoperso(models.Model):
	m_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
	m_nom = models.CharField(max_length=64, blank=True, null=True)
	m_prenom = models.CharField(max_length=64, blank=True, null=True)
	m_villeresidence = models.CharField(max_length=64, blank=True, null=True)
	m_email = models.EmailField(max_length=254, blank=True, null=True)
	#PhoneField est une application prise ici https://pypi.org/project/django-phone-field/
	m_telephone = PhoneField(blank=True, help_text='Contact phone number', null=True)

class Diploma(models.Model):
	m_user = models.ForeignKey(User,on_delete = models.CASCADE,blank = True,null = True)
	m_diploma = models.CharField(max_length = 64)
	m_school = models.CharField(max_length = 64,blank = True,null = True)
	m_year = models.IntegerField(blank = True, null = True)
	m_mention = models.CharField(max_length = 64,blank = True, null = True)
	m_intitule = models.CharField(max_length = 64,blank = True, null = True)
	m_date = models.DateTimeField(auto_now=True,blank=True,null = True)

class Competence(models.Model):
	m_user = models.ForeignKey(User,on_delete = models.CASCADE,blank = True,null = True)
	m_competence = models.CharField(max_length = 64) 
	m_date = models.DateTimeField(auto_now=True,blank=True,null = True)

class Experience(models.Model):
	m_user = models.ForeignKey(User,on_delete = models.CASCADE,blank = True,null = True)
	m_etablissement = models.CharField(max_length = 64)
	m_tasks = models.TextField(max_length = 256,blank = True,null = True)
	m_poste = models.TextField(max_length = 256,blank = True,null = True)
	m_start = models.DateField(blank = True, null = True)	
	m_end = models.DateField(blank = True, null = True)	
	m_date = models.DateTimeField(auto_now=True,blank=True,null = True)
	def tasks_enumerate(self):
		return self.m_tasks.split('\n')

class Biographie(models.Model):
	m_user = models.ForeignKey(User,on_delete = models.CASCADE,blank = True,null = True)
	m_description = models.TextField(max_length = 256)
	m_date = models.DateTimeField(auto_now=True,blank=True,null = True)

class Loisir(models.Model):
	m_user = models.ForeignKey(User,on_delete = models.CASCADE,blank = True,null = True)
	m_loisir = models.CharField(max_length = 64)
	m_date = models.DateTimeField(auto_now=True,blank=True,null = True)

class CVFolder(models.Model):
	m_user = models.ForeignKey(User,on_delete = models.CASCADE,blank = True,null = True)
	m_infoperso = models.ForeignKey(Infoperso,on_delete = models.CASCADE, blank = True, null = True)
	m_diplomas = models.ManyToManyField(Diploma,blank = True)
	m_loisirs = models.ManyToManyField(Loisir,blank = True)
	m_competences = models.ManyToManyField(Competence,blank = True)
	m_experiences = models.ManyToManyField(Experience,blank = True)
	m_date = models.DateTimeField(auto_now=True,blank=True,null = True)
