from django.db import models

class Pet(models.Model):
	SEXO = (
		('M', 'Masculino'),
		('F', 'Feminino')
		)
	nome = models.CharField(max_length=200)
	cpf_dono = models.CharField(max_length=200, blank=True, null=True)
	nadcimento  = models.DateField()
	raca = models.CharField(max_length=200, blank=True, null=True)
	sexo = models.CharField(max_length=1,choices=SEXO, blank=True, null=True)
	cor = models.CharField(max_length=200, blank=True, null=True)
	def __str__(self):
		return self.nome

class Atendimento(models.Model):
	TIPO =(
		('BANHO_E_TOSA', 'Banho e Tosa'),
		('CONSULTA', 'Consulta'),
		('CIRURGIA', 'Cirurgia'),
		('EXAME', 'Exame'),
		)
	pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='atendimentos')
	data_hora = models.DateTimeField(auto_now_add=False)
	procedimeto = models.CharField(max_length=256, null=True, blank=True)
	tipo = models.CharField(max_length=20, choices=TIPO)
	def __str__(self):
		return str(self.data_hora)

class Medicamento(models.Model):
	atendimento = models.ForeignKey(Atendimento, on_delete=models.CASCADE, related_name='medicamentos')
	nome = models.CharField(max_length=256)
	dose = models.CharField(max_length=256, null=True, blank=True)
	frequencia = models.CharField(max_length=256, null=True, blank=True)
	perido = models.CharField(max_length=256, null=True, blank=True)
	def __str__(self):
		return self.nome