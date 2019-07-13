from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.UserList.as_view(), name=views.UserList.name),
    path('user/<int:pk>/', views.UserDetail.as_view(), name=views.UserDetail.name),
    path('pet/', views.PetList.as_view(), name=views.PetList.name),
    path('pet/<int:pk>/', views.PetDetail.as_view(), name=views.PetDetail.name),
    path('atendimento/', views.AtendimentoList.as_view(), name=views.AtendimentoList.name),
    path('atendimento/<int:pk>/', views.AtendimentoDetail.as_view(), name=views.AtendimentoDetail.name),
    path('medicamento/', views.MedicamentoList.as_view(), name=views.MedicamentoList.name),
    path('medicamento/<int:pk>/', views.MedicamentoDetail.as_view(), name=views.MedicamentoDetail.name),    
]