from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'pk', 'username','email','password')

class AtendimentoSerializer(serializers.HyperlinkedModelSerializer):
	pet = serializers.SlugRelatedField(queryset=Pet.objects.all(), slug_field='cpf_dono')
	class Meta:
		model = Atendimento
		fields = ('url', 'pk', 'pet','data_hora', 'procedimeto', 'tipo')

class PetSerializer(serializers.HyperlinkedModelSerializer):
	atendimento = AtendimentoSerializer(many=True, read_only=True)
	class Meta:
		model = Pet
		fields = ('url', 'pk', 'nome','cpf_dono', 'nadcimento','raca', 'sexo', 'cor', 'atendimento')

class MeticamentoSerializer(serializers.HyperlinkedModelSerializer):
	#atendimento = serializers.SlugRelatedField(queryset=Atendimento.objects.all(), slug_field='id')
	class Meta:
		model = Medicamento
		fields = ('url', 'pk', 'atendimento', 'nome','dose', 'frequencia', 'perido')