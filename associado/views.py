from rest_framework import viewsets
from rest_framework import permissions, authentication

from .models import Associado
from .serializers import AssociadoSerializer


class AssociadoViewSet(viewsets.ModelViewSet):
    serializer_class = AssociadoSerializer

    # CONFIGURAR PARA SÓ EXIBIR SE ESTIVER AUTENTICADO COM TOKEN
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [
    #         authentication.TokenAuthentication, 
    #         authentication.SessionAuthentication
    #     ]
    def get_queryset(self):
        queryset = Associado.objects.all()

        return queryset