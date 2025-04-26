from rest_framework import serializers
from .models import Candidat, Recruteur

class CandidatSerializer(serializers.ModelSerializer):
    recruteur_detail = serializers.StringRelatedField(source='recruteur', read_only=True)

    class Meta:
        model = Candidat
        fields = ['id', 'nom', 'prenom', 'email', 'recruteur', 'recruteur_detail']

class RecruteurSerializer(serializers.ModelSerializer):
    candidats = CandidatSerializer(many=True, read_only=True)

    class Meta:
        model = Recruteur
        fields = ['id', 'nom', 'entreprise', 'email', 'candidats']
