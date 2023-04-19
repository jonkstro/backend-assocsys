from rest_framework import viewsets
from rest_framework import permissions, authentication

from associado.models import Associado

from .models import Carteira
from .serializers import CarteiraSerializer

# Importações necessárias para realizar manipulação da imagem da carteira:
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from PIL import Image, ImageDraw, ImageFont
import sys

# Demais importações necessárias
from django.conf import settings
import os
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.views import Response


class CarteiraViewSet(viewsets.ModelViewSet):
    serializer_class = CarteiraSerializer

    # CONFIGURAR PARA SÓ EXIBIR SE ESTIVER AUTENTICADO COM TOKEN
    # permission_classes = [permissions.IsAuthenticated]
    # authentication_classes = [
    #         authentication.TokenAuthentication,
    #         authentication.SessionAuthentication
    #     ]
    def get_queryset(self):
        queryset = Carteira.objects.all()

        return queryset

    # TODO: CRIAR FUNÇÃO DE GERAR OS CARTÕES.


# FUNÇÃO QUE IRÁ EDITAR AS CARTEIRAS E COLOCAR O NOME DE TODOS ASSOCIADOS, 
# APÓS ISSO IRÁ SALVAR A IMAGEM DA CARTEIRA EDITADA NA MODEL CARTEIRA.

    def gerar_carteiras(self):
        # Pegando o path do certificado
        path_template = os.path.join(
            settings.BASE_DIR, 'templates/static/img/template_certificado.png'
        )
        # Pegando o path da fonte que será usada
        path_fonte = os.path.join(
            settings.BASE_DIR, 'templates/static/fontes/arimo.ttf'
        )

        for associado in Associado.all():
            # Abrindo a imagem base do certificado
            img = Image.open(path_template)
            # Aqui começa a editar a imagem
            draw = ImageDraw.Draw(img)
            # Configurando a fonte que irá ser usada na imagem
            fonte_nome = ImageFont.truetype(path_fonte, 60)
            # Configurando outra fonte que será usada
            fonte_info = ImageFont.truetype(path_fonte, 30)
            # Editando a imagem com a fonte de nome
            draw.text((230, 651),
                      f"{associado.nome}",
                      font=fonte_nome,
                      fill=(0, 0, 0)
                      )
            # Editando a imagem com a fonte de info (secundária)
            draw.text((761, 782),
                      f"{associado.cpf}",
                      font=fonte_info,
                      fill=(0, 0, 0)
                      )
            # Editando a imagem com a fonte de info
            draw.text((816, 849),
                      f"{associado.matricula} horas",
                      font=fonte_info,
                      fill=(0, 0, 0)
                      )
            # Salvando a imagem em memória ???
            output = BytesIO()
            # Salvando a imagem editada em formato PNG na memória
            img.save(output, format="PNG", quality=100)
            output.seek(0)
            img_final = InMemoryUploadedFile(output,
                                             # Descrevendo a forma que irá ser salva a imagem:
                                             'ImageField',  # A imagem será ImageField;
                                             # Será salva com a matricula + '.png'
                                             f'{associado.matricula}.png',
                                             # Demais configurações: Procurar no Google.
                                             'image/jpeg',
                                             sys.getsizeof(output),
                                             None)
            # Aqui é instanciado o novo certificado com os dados
            carteira_gerada = Carteira(
                carteira=img_final,
                associado=associado,
            )
            carteira_gerada.save()
            return Response('Sucessagem', status=HTTP_201_CREATED)


#TODO: Testar a função acima e criar outra função pra fazer unitario