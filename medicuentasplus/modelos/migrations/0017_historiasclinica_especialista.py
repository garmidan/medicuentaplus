# Generated by Django 2.1.5 on 2021-09-29 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0016_diagnostico_codigo'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiasclinica',
            name='especialista',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modelos.Usuario'),
        ),
    ]
