from rest_framework import serializers

from associado.models import Associado


class AssociadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Associado
        fields = '__all__'


# REALIZAR A VALIDAÇÃO DO CAMPO CPF, PARA QUE ELE NÃO TENHA MENOS DE 14 CARACS.
    def validate_cpf(self, value):
        if len(value) != 14:
            raise serializers.ValidationError('CPF inválido')
        else:
            return value