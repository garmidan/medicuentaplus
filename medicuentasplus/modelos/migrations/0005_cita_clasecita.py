# Generated by Django 2.1.5 on 2021-09-13 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0004_cita_tipodocumento'),
    ]

    operations = [
        migrations.AddField(
            model_name='cita',
            name='clasecita',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]