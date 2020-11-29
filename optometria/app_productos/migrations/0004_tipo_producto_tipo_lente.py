# Generated by Django 3.1.3 on 2020-11-29 22:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_productos', '0003_tipo_lente'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipo_producto',
            name='tipo_lente',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lentes', to='app_productos.tipo_lente'),
        ),
    ]