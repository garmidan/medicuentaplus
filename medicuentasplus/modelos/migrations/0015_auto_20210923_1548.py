# Generated by Django 2.1.5 on 2021-09-23 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0014_auto_20210923_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consulta',
            name='diagnostico',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
