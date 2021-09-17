# Generated by Django 2.1.5 on 2021-09-14 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0011_auto_20210914_1025'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaconsulta', models.DateField(blank=True, null=True)),
                ('fechaalta', models.TimeField(blank=True, null=True)),
                ('diagnostico', models.CharField(blank=True, max_length=1000, null=True)),
                ('tratamiento', models.TextField(blank=True, null=True)),
                ('otrosdatos', models.TextField(blank=True, null=True)),
                ('observaciones', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='diagnostico',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='fechaalta',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='fechaconsulta',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='observaciones',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='otrosdatos',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='tratamiento',
        ),
        migrations.AddField(
            model_name='consulta',
            name='historiaclinicas',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='modelos.HistoriasClinica'),
        ),
    ]
