from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

def home(request):
    return HttpResponse("Bienvenue sur la page d'accueil de notre API !")

schema_view = get_schema_view(
    openapi.Info(
        title="Recrutement API",
        default_version='v1',
        description="API pour gestion des candidats et recruteurs",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),  
    path('api/', include('api.urls')),  
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='api-docs'),  
   
]

