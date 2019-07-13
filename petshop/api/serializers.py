from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'pk', 'username','email','password')

class MeticamentoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Medicamento
		fields = ('url', 'pk', 'atendimento', 'nome','dose', 'frequencia', 'perido')        

class AtendimentoSerializer(serializers.HyperlinkedModelSerializer):
	pet = serializers.SlugRelatedField(queryset=Pet.objects.all(), slug_field='cpf_dono')
	medicamentos = MeticamentoSerializer(many=True, read_only=True)
	class Meta:
		model = Atendimento
		fields = ('url', 'pk', 'pet','data_hora', 'procedimeto', 'tipo', 'medicamentos')

class PetSerializer(serializers.HyperlinkedModelSerializer):
	atendimentos = AtendimentoSerializer(many=True, read_only=True)
	class Meta:
		model = Pet
		fields = ('url', 'pk', 'nome','cpf_dono', 'nadcimento','raca', 'sexo', 'cor', 'atendimentos')

