from django.db import models

class Recruteur(models.Model):
    nom = models.CharField(max_length=100)
    entreprise = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nom} ({self.entreprise})"

class Candidat(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField()
    recruteur = models.ForeignKey(Recruteur, on_delete=models.CASCADE, related_name='candidats')

    def __str__(self):
        return f"{self.prenom} {self.nom}"
