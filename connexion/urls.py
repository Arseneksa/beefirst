from django.urls import path,  include
from . import views
from django.conf import settings

#app_name = 'CreateCV'
urlpatterns = [
    path('', views.connexion, name="connexion"),

    path('inscription/',views.inscription, name="inscription"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('qrcode/',views.qrcode, name="qrcode"),
    path('logout1/',views.logout1, name="logout1"),
    path('contact/',views.contact, name="contact")

    ]
