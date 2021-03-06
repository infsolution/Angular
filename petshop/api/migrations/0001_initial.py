# Generated by Django 2.2.3 on 2019-07-13 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField()),
                ('procedimeto', models.CharField(blank=True, max_length=256, null=True)),
                ('tipo', models.CharField(choices=[('BANHO_E_TOSA', ''), ('CONSULTA', ''), ('CIRURGIA', ''), ('EXAME', '')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('cpf_dono', models.CharField(blank=True, max_length=200, null=True)),
                ('nadcimento', models.DateField()),
                ('raca', models.CharField(blank=True, max_length=200, null=True)),
                ('sexo', models.CharField(blank=True, choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1, null=True)),
                ('cor', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Medicamento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=256)),
                ('dose', models.CharField(blank=True, max_length=256, null=True)),
                ('frequencia', models.CharField(blank=True, max_length=256, null=True)),
                ('perido', models.CharField(blank=True, max_length=256, null=True)),
                ('atendimento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atendimento', to='api.Atendimento')),
            ],
        ),
        migrations.AddField(
            model_name='atendimento',
            name='pet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='atendimento', to='api.Pet'),
        ),
    ]
