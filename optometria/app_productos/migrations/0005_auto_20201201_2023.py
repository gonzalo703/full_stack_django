# Generated by Django 3.1.3 on 2020-12-01 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_productos', '0004_tipo_producto_tipo_lente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipo_lente',
            name='distancia',
        ),
        migrations.RemoveField(
            model_name='tipo_lente',
            name='lado',
        ),
        migrations.AddField(
            model_name='tipo_lente',
            name='cerca',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='tipo_lente',
            name='derecha',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='tipo_lente',
            name='izquierda',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='tipo_lente',
            name='lejos',
            field=models.BooleanField(null=True),
        ),
        migrations.AlterField(
            model_name='tipo_lente',
            name='armazon',
            field=models.BooleanField(null=True),
        ),
    ]