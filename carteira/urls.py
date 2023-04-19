from django.urls import path
from .views import GerarCarteirasView

urlpatterns = [
    path('gerar-carteiras/all/', GerarCarteirasView.as_view(), name='gerar_carteiras'),
]
