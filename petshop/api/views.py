from django.shortcuts import render
from django.http import HttpResponse
from django_filters import rest_framework as filters
from rest_framework import permissions
from rest_framework import generics
from .serializers import *
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

class UserList(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	def perform_create(self, serializer):
		instance = serializer.save()
		instance.set_password(instance.password)
		instance.save()
	name = 'user-list'
	
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAuthenticated,)
	name = 'user-detail'

class PetList(generics.ListCreateAPIView):
	queryset = Pet.objects.all()
	serializer_class = PetSerializer
	filter_backends = (filters.DjangoFilterBackend,)
	permission_classes = (permissions.IsAuthenticated,)
	filter_fields = '__all__'
	name = 'pet-list'
	
class PetDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Pet.objects.all()
	serializer_class = PetSerializer
	permission_classes = (permissions.IsAuthenticated,)
	name = 'pet-detail'

class AtendimentoList(generics.ListCreateAPIView):
	queryset = Atendimento.objects.all()
	serializer_class = AtendimentoSerializer
	permission_classes = (permissions.IsAuthenticated,)
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = '__all__'
	name = 'atendimento-list'
	
class AtendimentoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Atendimento.objects.all()
	serializer_class = AtendimentoSerializer
	permission_classes = (permissions.IsAuthenticated,)
	name = 'atendimento-detail'

class MedicamentoList(generics.ListCreateAPIView):
	queryset = Medicamento.objects.all()
	serializer_class = MeticamentoSerializer
	permission_classes = (permissions.IsAuthenticated,)
	filter_backends = (filters.DjangoFilterBackend,)
	filter_fields = '__all__'
	name = 'medicamento-list'
	
class MedicamentoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Medicamento.objects.all()
	serializer_class = MeticamentoSerializer
	permission_classes = (permissions.IsAuthenticated,)
	name = 'medicamento-detail'