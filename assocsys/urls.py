
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers

from .views import UserActivationView
from associado.views import AssociadoViewSet
from carteira.views import CarteiraViewSet

# importações para trabalhar com imagens
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
# SEMPRE APÓS DEFINIR UM get_queryset TEMOS QUE DIZER SEU BASENAME
router.register(r'associados', AssociadoViewSet, basename='Associado')
router.register(r'carteiras', CarteiraViewSet, basename='Carteira')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # Views de autenticação do DJOSER
    path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
    # path('auth/', include('djoser.social.urls')),
    # View de ativação do usuário ao clicar no link enviado pelo djoser:
    path('activate/<str:uid>/<str:token>/', UserActivationView.as_view()),
    # Views da carteira (Criar carteira coletiva, individual, etc...)
    path('carteira/', include('carteira.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # para caso vá trabalhar com imagens
