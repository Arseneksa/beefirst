
from django.shortcuts import render,redirect,HttpResponse
from django.http import JsonResponse
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required 
from django.contrib.auth.models import User



#Création utilisateur temporaire
#user = User.objects.create_user('john', 'lennon@thebeatles.com', 'password')
#user.save()

def home(request):

    #authentification de l'utilisateur
    # Nous vérifions si les données sont correctes
    user = authenticate(username='john', password='password')
    if user:  # Si l'objet renvoyé n'est pas None
        request.session['user_id'] = request.user.id
        login(request, user)  # nous connectons l'utilisateur
        print(request.user.id)
    else:  # sinon une erreur sera affichée
        error = True
    return render(request, 'create_cv/accueil.html', {'nbar': 'home'})


@login_required(login_url='create_cv/')
def infoperso(request):
    
    mesinfos = {}
    if Infoperso.objects.filter(m_user=request.user):
        infos = Infoperso.objects.filter(m_user=request.user)
        mesinfos = infos.first()
        text = "Modifier"
    else :
        text = "Ajouter"

    context = {
        'menu': 'infoperso',
        'text': text,
        'mesinfos': mesinfos,
        'infoperso': Infoperso.objects.filter(),
        'diplomas': Diploma.objects.filter(),
        'competence': Competence.objects.all(),
        'experiences': Experience.objects.filter(),
        'biographie': Biographie.objects.last(),
        'loisirs': Loisir.objects.filter(),
        'nbar': 'infoperso'
    }
    return render(request, 'create_cv/infoperso.html', context)
    

@login_required(login_url='create_cv/')
def diplome(request):
    #Création ou recuperation du CV de l'utilisateur

    cv = CVFolder.objects.get(m_user=request.user)

    if cv:
        print(cv)

    else:
        cv = CVFolder(m_user=request.user)
        cv.save()
        print(cv)

    context = {
        'menu': 'diplome',
     	'infoperso': Infoperso.objects.filter(),
     	'diplomas': Diploma.objects.filter(),
        'competence': Competence.objects.all(),
        'experiences': Experience.objects.filter(),
        'biographie': Biographie.objects.last(),
      	'loisirs': Loisir.objects.filter(),
        'nbar': 'diplome'
    }
    return render(request, 'create_cv/diplome.html', context)


@login_required(login_url='create_cv/')
def competence(request):
    context = {
        'menu': 'competence',
     	'infoperso': Infoperso.objects.filter(),
     	'diplomas': Diploma.objects.filter(),
        'competence': Competence.objects.all(),
        'experiences': Experience.objects.filter(),
        'biographie': Biographie.objects.last(),
      	'loisirs': Loisir.objects.filter(),
        'nbar': 'competence'
    }
    return render(request, 'create_cv/competence.html', context)


@login_required(login_url='create_cv/')
def experience(request):
    context = {
        'menu': 'experience',
     	'infoperso': Infoperso.objects.filter(),
     	'diplomas': Diploma.objects.filter(),
        'competence': Competence.objects.all(),
        'experiences': Experience.objects.filter(),
        'biographie': Biographie.objects.last(),
      	'loisirs': Loisir.objects.filter(),
        'nbar': 'experience'
    }
    return render(request, 'create_cv/experience.html', context)


@login_required(login_url='create_cv/')
def biographie(request):
    context = {
        'menu': 'biographie',
        'infoperso': Infoperso.objects.filter(),
     	'diplomas': Diploma.objects.filter(),
        'competence': Competence.objects.all(),
        'experiences': Experience.objects.filter(),
        'biographie': Biographie.objects.last(),
      	'loisirs': Loisir.objects.filter(),
        'nbar': 'biographie'
    }
    return render(request, 'create_cv/biographie.html', context)


@login_required(login_url='create_cv/')
def loisir(request):
    context = {
        'menu': 'loisir',
     	'infoperso': Infoperso.objects.filter(),
     	'diplomas': Diploma.objects.filter(),
        'competence': Competence.objects.all(),
        'experiences': Experience.objects.filter(),
        'biographie': Biographie.objects.last(),
      	'loisirs': Loisir.objects.filter(),
        'nbar': 'loisir'
    }
    return render(request, 'create_cv/loisir.html', context)


@login_required(login_url='create_cv/')
def voir_cv(request):
    context = {
        'infoperso': Infoperso.objects.filter(),
     	'diplomas': Diploma.objects.filter(),
        'competence': Competence.objects.all(),
        'experiences': Experience.objects.filter(),
        'biographie': Biographie.objects.last(),
      	'loisirs': Loisir.objects.filter(),

    }
    return render(request, 'apercu_cv/modele1/base1.html', context)


def save(request,page):

    if page == 'infoperso':
        if Infoperso.objects.filter(m_user=request.user):
            infoperso = Infoperso.objects.get(m_user=request.user)
            infoperso.m_nom = request.POST['nom']
            infoperso.m_prenom = request.POST['prenom']
            infoperso.m_villeresidence = request.POST['ville']
            infoperso.m_email = request.POST['email']
            infoperso.m_telephone = request.POST['telephone']
        else:
            print(request.POST['infoperso']+'\n')
            infoperso = Infoperso(m_user=request.user, m_nom=request.POST['nom'], m_prenom=request.POST['prenom'],
                                m_villeresidence=request.POST['ville'], m_email=request.POST['email'], 
                                m_telephone=request.POST['telephone'])
            infoperso.save()
        return redirect('/create_cv/infoperso')

    elif page == 'diplome':
        print(request.POST['diplome']+'\n')
        diploma = Diploma(m_user= request.user, m_diploma=request.POST['diplome'], m_intitule=request.POST['intitule'],m_school=request.POST["ecole"],m_year=request.POST["annee"],m_mention=request.POST["mention"])
        diploma.save()
        return redirect('/create_cv/diplome')

    elif page == 'competence':
        print(request.POST['competence']+'\n')
        competence = Competence(m_user= request.user, m_competence=request.POST['competence'])
        competence.save()
        return redirect('/create_cv/competence')

    elif page == 'experience':
        experience = Experience(m_user= request.user, m_etablissement=request.POST['etablissement'], m_poste=request.POST['poste'],m_tasks=request.POST["tasks"],m_start=request.POST["start"],m_end=request.POST["end"])
        experience.save()
        return redirect('/create_cv/experience')

    elif page == 'biographie':
        test = Biographie.objects.get(m_user = request.user)
        if test :
            test.m_description = request.POST['biographie']
            
            return redirect('/create_cv/biographie')
        else:
            biographie = Biographie(m_user= request.user, m_description=request.POST['biographie'])
            biographie.save()
            return redirect('/create_cv/biographie')

    elif page == 'loisir':
        loisir = Loisir(m_user= request.user, m_loisir=request.POST['loisir'])
        loisir.save()
        return redirect('/create_cv/loisir')	

def delete(request,page,id):
    if page == 'diplome':
        
        print(id)

        diploma = Diploma.objects.get(id = id)
        diploma.delete()
        
        print("Diplome supprimé avec succès")

        return redirect('/create_cv/diplome')
    elif page == 'competence':
        
        competence = Competence.objects.get(id = id)
        competence.delete()

        print("Compétence supprimé avec succès")

        return redirect('/create_cv/competence')

    elif page == 'experience':

        experience = Experience.objects.get(id = id)
        experience.delete()

        print("Expérience supprimée avec succès")
        return redirect('/create_cv/experience')

    elif page == 'biographie':

        biographie = Biographie.objects.get(id = id)
        biographie.delete()

        print("Biographie supprimé avec succès")

        return redirect('/create_cv/biographie')	
    elif page == 'loisir':	

        loisir = Loisir.objects.get(id = id)
        loisir.delete()

        print("Loisir supprimé avec succès")

        return redirect('/create_cv/loisir')	

def enregistrer(request,page):
    if page == 'infoperso':
        #print(request.POST['infoperso']+'\n')
        """ infoperso = Infoperso(m_user=request.user, m_nom=request.POST['nom'], m_prenom=request.POST['prenom'],
                              m_villeresidence=request.POST['ville'], m_email=request.POST['email'], 
                              m_telephone=request.POST['telephone'])
        infoperso.save() """
        return redirect('/create_cv/diplome')
    
    elif page == 'diplome':
        diplomes = Diploma.objects.filter(m_user = request.user)
        cv = CVFolder.objects.get(m_user = request.user)
        for diplome in diplomes : 
            cv.m_diplomas.add(diplome)

            print (cv.m_diplomas.all())
            print("Diplome {} enregistré avec succès".format(diplome))
        succes = 1
        return redirect('/create_cv/experience',{'succes': succes})

    elif page == 'competence':
        competences = Competence.objects.filter(m_user = request.user)
        cv = CVFolder.objects.get(m_user = request.user)
        for competence in competences : 
            cv.m_competences.add(competence)

            print (cv.m_competences.all())
            print("Competence {} enregistré avec succès".format(competence))
        succes = 1
        return redirect('/create_cv/loisir',{'succes': succes})

    elif page == 'experience':	

        #experience = Experience.objects.get(id = id)
        experiences = Experience.objects.filter(m_user = request.user)
        cv = CVFolder.objects.get(m_user = request.user)
        for experience in experiences : 
            cv.m_experiences.add(experience)

            print (cv.m_experiences.all())
            print("Experience {} enregistré avec succès".format(experience))
        succes = 1
        return redirect('/create_cv/competence',{'succes': succes})

    elif page == 'biographie':
        biographies = Biographie.objects.filter(m_user = request.user)
        cv = CVFolder.objects.get(m_user = request.user)
        for biographie in biographies : 
            
            cv.m_biographies.add(biographie)

            print (cv.m_biographies.all())
            print("Biographie {} enregistré avec succès".format(biographie))
        succes = 1
        return redirect('/create_cv/biographie', {'succes': succes})

    elif page == 'loisir':
        #loisir = Loisir.objects.get(id = id)
        loisirs = Loisir.objects.filter(m_user = request.user)
        cv = CVFolder.objects.get(m_user = request.user)
        for loisir in loisirs : 
            cv.m_loisirs.add(loisir)

            print (cv.m_loisirs.all())
            print("Loisir {} enregistré avec succès".format(loisir))
        succes = 1
        return redirect('/create_cv/biographie', {'succes': succes})
