from django.db import models
from django.utils import timezone

# Create your models here.
class Article(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.CharField(max_length=30)

class Produit(models.Model):
    nom = models.CharField(max_length=200)
    description = models.TextField()
    prix = models.DecimalField(max_digits=8, decimal_places=2)
    stock_disponible = models.PositiveIntegerField()
    image = models.ImageField(upload_to='produits/')

class Tache(models.Model):
    STATUT_CHOICES = (
        ('en_cours', 'En cours'),
        ('terminee', 'Terminée'),
        ('en_attente', 'En attente'),
    )

    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_creation = models.DateTimeField(auto_now_add=True)
    date_echeance = models.DateField()
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES)

class UserProfile(models.Model):
    user = models.CharField(max_length=25)
    email = models.EmailField(max_length=40)
    password = models.CharField(max_length=25)
    date_created = models.DateTimeField(auto_now_add=True)
    profile_photo = models.ImageField(upload_to='profile_photos')

class Event(models.Model):
    title = models.CharField(max_length=200)
    start_datetime = models.DateTimeField(default=timezone.now)
    end_datetime = models.DateTimeField(default=timezone.now)
    location = models.CharField(max_length=200)
    description = models.TextField()