from rest_framework import generics
from .models import Candidat, Recruteur
from .serializers import CandidatSerializer, RecruteurSerializer

class CandidatCreateView(generics.CreateAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer

class CandidatDetailView(generics.RetrieveAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer

class RecruteurCandidatListView(generics.ListAPIView):
    queryset = Candidat.objects.all()
    serializer_class = CandidatSerializer

class RecruteurDetailView(generics.RetrieveAPIView):
    queryset = Recruteur.objects.all()
    serializer_class = RecruteurSerializer
