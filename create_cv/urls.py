from django.urls import path
from . import views
from django.conf import settings

#app_name = 'CreateCV'
urlpatterns = [
    path('',views.home, name="home"),
    path('infoperso/', views.infoperso, name="infoperso"),
    path('diplome/', views.diplome, name="diplome"),
    path('experience/', views.experience , name="experience"),
    path('biographie/', views.biographie, name="biographie"),
    path('reference/', views.reference, name="reference"),
    path('loisir/' , views.loisir , name="loisir"),
    path('langue/' , views.langue , name="langue"),
    path('competence/' , views.competence , name="competence"),
    path('voir_cv/' , views.voir_cv , name="voir_cv"),
    path('save/<slug:page>',views.save, name="save"),
    path('photo/',views.photo, name="photo"),
    path('enregistrer/<slug:page>',views.enregistrer, name="enregistrer"),
    path('delete/<slug:page>/<int:id>',views.delete, name="delete"),
    path('modifier/<slug:page>/<int:id>',views.modifier, name="modifier"),
    path('save_edit/<slug:page>/<int:id>',views.save_edit, name="save_edit")

    ]
