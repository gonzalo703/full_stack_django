# Generated by Django 3.1.3 on 2020-11-29 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('apellido', models.CharField(max_length=64)),
                ('dni', models.IntegerField()),
                ('telefono', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Turno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_turno', models.DateTimeField()),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medico', to='app_optometria.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='paciente', to='app_optometria.paciente')),
            ],
        ),
        migrations.CreateModel(
            name='Historia_clinica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historia_clinica', models.CharField(max_length=500)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medicos', to='app_optometria.medico')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pacientes', to='app_optometria.paciente')),
            ],
        ),
    ]
