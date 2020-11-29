# Generated by Django 3.1.3 on 2020-11-29 21:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_optometria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Forma_pago',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('forma_pago', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=64)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categoria', to='app_productos.tipo_producto')),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('fecha', models.DateField(auto_now_add=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cliente', to='app_optometria.paciente')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='estados', to='app_productos.estado')),
                ('forma_pago', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pago', to='app_productos.forma_pago')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to='app_productos.producto')),
            ],
        ),
    ]