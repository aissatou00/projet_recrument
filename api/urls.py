from django.urls import path
from django.http import JsonResponse
from .views import CandidatCreateView, CandidatDetailView, RecruteurCandidatListView, RecruteurDetailView

def api_home(request):
    return JsonResponse({
        "message": "Bienvenue sur l'API Recrutement",
        "endpoints": [
            "/api/candidat/create/",
            "/api/candidat/<int:pk>/",
            "/api/recruteur/candidats/",
            "/api/recruteur/<int:pk>/"
        ]
    })

urlpatterns = [
    path('', api_home, name='api-home'),  
    path('candidat/create/', CandidatCreateView.as_view(), name='candidat-create'),
    path('candidat/<int:pk>/', CandidatDetailView.as_view(), name='candidat-detail'),
    path('recruteur/candidats/', RecruteurCandidatListView.as_view(), name='recruteur-candidats'),
    path('recruteur/<int:pk>/', RecruteurDetailView.as_view(), name='recruteur-detail'),
]
