# Generated by Django 2.1.5 on 2021-09-13 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0007_auto_20210913_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='historiasclinica',
            name='ocupacion',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
