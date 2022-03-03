from django.db import models
from django.contrib.auth.models import User
#from phone_field import PhoneField
#from phonenumber_field.modelfields import PhoneNumberField


class Infoperso(models.Model):
    m_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    m_nom = models.CharField(max_length=64, blank=True, null=True)
    m_prenom = models.CharField(max_length=64, blank=True, null=True)
    m_villeresidence = models.CharField(max_length=64, blank=True, null=True)
    m_email = models.EmailField(max_length=254, blank=True, null=True)

    m_age = models.IntegerField(null=True)
    m_profession = models.CharField(max_length=254, null=True)

    m_telephone = models.IntegerField(blank=True, help_text='Numero de telephone', null=True)

    class Meta:
        ordering = ['m_nom']
    def __str__(self):
        return '%s' % (self.m_email)


class Photo(models.Model):
    m_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    m_user_avatar = models.ImageField(upload_to="media/createcv/", blank=True)

    class Meta:
        ordering = ['m_user_avatar']
    def __str__(self):
        return '%s' % (self.m_user_avatar)



#Concerne le type de diposition que aura le contenu du cv
"""class DispositionCv(models.Model):
    # cv_numero = models.IntegerField(blank=True)
    #couleur du cv
    nom = models.CharField(blank=True,max_length=256)
    #Le type de cv (professionnel, simple, Experimenté)
    cv_type = models.CharField(blank=True,max_length=256)
    #Le modèle correspond au type
    cv_img = models.ImageField(upload_to="media/modelecv/", blank=True)"""
# Table permettant de créer des modèle de cv
class Cvmodel(models.Model):
    # cv_numero = models.IntegerField(blank=True)
    nom = models.CharField(blank=True,max_length=256)
    #couleur du cv
    cv_color = models.CharField(blank=True,max_length=256)
    #Le type de cv (professionnel, simple, Experimenté)
    cv_type = models.CharField(blank=True,max_length=256)


#Image correspondant au modèle de cv
class CvImg(models.Model):
    m_model = models.ForeignKey(Cvmodel, on_delete=models.CASCADE, blank=True, null=True)
    nom = models.ImageField(upload_to="media/modelecv/", blank=True)

#Table permettant de lier le modèle  de cv choisi à l'utilisateur
class Cvsetting(models.Model):
    m_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    cv_model = models.ForeignKey(Cvmodel, on_delete=models.CASCADE, blank=True, null=True)


class Diploma(models.Model):
    m_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='diplomes', blank=True, null=True)
    m_diploma = models.CharField(max_length=64)
    m_school = models.CharField(max_length=64, blank=True, null=True)
    m_year = models.IntegerField(blank=True, null=True)
    m_mention = models.CharField(max_length=64, blank=True, null=True)
    m_intitule = models.CharField(max_length=64, blank=True, null=True)
    # m_aide = models.CharField(max_length=5000, blank=True, null=True)

    m_date = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        ordering = ['m_diploma']
    def __str__(self):
        return '%s' % (self.m_diploma)

class Competence(models.Model):
    m_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    m_competence = models.CharField(max_length=64)
    # m_aide = models.CharField(max_length=5000, blank=True, null=True)
    m_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ['m_competence']
    def __str__(self):
        return '%s' % (self.m_competence)

class Langue(models.Model):
    m_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    m_nom = models.CharField(max_length=64)
    # m_aide = models.CharField(max_length=5000, blank=True, null=True)
    m_niveau = models.CharField(max_length=64)
    class Meta:
        ordering = ['m_nom']
    def __str__(self):
        return '%s' % (self.m_nom)


class Experience(models.Model):
    m_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    m_etablissement = models.CharField(max_length=64)
    m_tasks = models.TextField(max_length=256, blank=True, null=True)
    m_poste = models.TextField(max_length=256, blank=True, null=True)
    m_start = models.DateField(blank=True, null=True)
    m_end = models.DateField(blank=True, null=True)
    # m_aide = models.CharField(max_length=5000, blank=True, null=True)
    m_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def tasks_enumerate(self):
        return self.m_tasks.split('\n')

    class Meta:
        ordering = ['m_poste']
    def __str__(self):
        return '%s' % (self.m_poste)

class Biographie(models.Model):
    m_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    m_description = models.TextField(max_length=256)
    # m_aide = models.CharField(max_length=5000, blank=True, null=True)
    m_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ['m_description']
    def __str__(self):
        return '%s' % (self.m_description)
class Reference(models.Model):
    m_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    m_description = models.TextField(max_length=256)
    # m_aide = models.CharField(max_length=5000, blank=True, null=True)
    m_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    def tasks_enumerate(self):
        return self.m_description.split('\n')

    class Meta:
        ordering = ['m_description']
    def __str__(self):
        return '%s' % (self.m_description)

class Loisir(models.Model):
    m_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    m_loisir = models.CharField(max_length=64)
    m_date = models.DateTimeField(auto_now=True, blank=True, null=True)

    class Meta:
        ordering = ['m_loisir']
    def __str__(self):
        return '%s' % (self.m_loisir)
class CVFolder(models.Model):
    m_user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='cv', blank=True, null=True)
    m_infoperso = models.ForeignKey(Infoperso, related_name='cv', on_delete=models.CASCADE, blank=True, null=True)
    m_diplomas = models.ManyToManyField(Diploma,related_name='cv', blank=True)
    m_loisirs = models.ManyToManyField(Loisir,related_name='cv',  blank=True)
    m_competences = models.ManyToManyField(Competence,related_name='cv',  blank=True)
    m_references = models.ManyToManyField(Reference, related_name='cv',  blank=True)
    m_experiences = models.ManyToManyField(Experience, related_name='cv',  blank=True)
    m_setting = models.ManyToManyField(Cvsetting, related_name='cv',  blank=True)
    m_photos = models.ManyToManyField(Photo, related_name='cv', blank=True)
    m_date = models.DateTimeField(auto_now=True, blank=True, null=True)
