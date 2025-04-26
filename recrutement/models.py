from django.db import models

# Create your models here.


class Recruteur(models.Model):
    nom = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom} - {self.entreprise}"

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    experience = models.TextField()
    recruteur = models.ForeignKey(Recruteur, on_delete=models.CASCADE, related_name='candidats', null=True, blank=True)

    def __str__(self):
        return self.nom
