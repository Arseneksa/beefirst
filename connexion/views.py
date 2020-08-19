from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
import nexmo


# Création utilisateur temporaire
# user = User.objects.create_user('john', 'lennon@thebeatles.com', 'password')
# user.save()
def inscription(request):
    # user = User.
    # if Photo.objects.filter(m_user=request.user):
    #     photos = Photo.objects.filter(m_user=request.user).first()
    err = ''
    errpass = ''
    if request.method == 'POST':
        if User.objects.filter(username=request.POST['email']):
            err = "Cette adresse  email est déja enregistrée veuillez saisir une autre adresse"

        elif request.POST['password'] == request.POST['comfirmpassword']:

            user1 = User.objects.create_user(username= ""+request.POST['email'], first_name=request.POST['name'],
                        email=request.POST['email'], password=request.POST['password'])
            user1.save()

            # authentification de l'utilisateur
            # Nous vérifions si les données sont correctes

            print(user1.email)
            user = authenticate(username=user1.email, password=user1.password)
            if user:  # Si l'objet renvoyé n'est pas None
                request.session['user_id'] = request.user.id
                login(request, user)  # nous connectons l'utilisateur
                print(request.user.id)
            else:  # sinon une erreur sera affichée
                error = True
            return render(request, 'create_cv/accueil.html', {'nbar': 'home'})

        else:
            errpass = 'Veillez saisir des mots de passe identique'

    return render(request, 'index.html', {'err': err, 'errpass': errpass})


def connexion(request):
    err = ''
    if request.method == 'POST':
        user = authenticate(username=''+request.POST['email'], password=""+request.POST['password'])
        if user is not None:  # Si l'objet renvoyé n'est pas None
            request.session['user_id'] = request.user.id
            login(request, user)  # nous connectons l'utilisateur
            print(request.user.id)
            return render(request, 'create_cv/accueil.html', {'nbar': 'home'})
        else:  # sinon une erreur sera affichée
            error = True
            err = 'Adresse email ou mot de passe incorrect'

    return render(request, 'login.html', {'err': err})


def qrcode(request):
    return render(request, 'qrcode.html')


def contact(request):
    success = ''
    client = nexmo.Client(key='49d42508', secret='Wsn3r3BCdvyApRAi')
    if request.method == 'POST':
        client.send_message({
            'from': 'BeeFirst',
            'to': '237698460369',
            'text': request.POST['nom'] + '\n' + request.POST['message'],
        })
        success = 'Merci de nous avoir contacté'
    return render(request, 'contact.html', {'success': success})


def logout1(request):
    logout(request)
    return render(request, 'create_cv/accueil.html', {'nbar': 'home'})
