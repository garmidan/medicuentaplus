# Generated by Django 2.1.5 on 2021-09-23 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0012_auto_20210914_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='permisoscomentario',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
