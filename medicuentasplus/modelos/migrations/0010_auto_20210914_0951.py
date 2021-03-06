# Generated by Django 2.1.5 on 2021-09-14 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelos', '0009_historiasclinica_parentescoresponsable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='historiasclinica',
            old_name='direccionAcompañante',
            new_name='diagnostico',
        ),
        migrations.RenameField(
            model_name='historiasclinica',
            old_name='horaatencion',
            new_name='fechaalta',
        ),
        migrations.RenameField(
            model_name='historiasclinica',
            old_name='fechaatencion',
            new_name='fechaconsulta',
        ),
        migrations.RenameField(
            model_name='historiasclinica',
            old_name='enfermedadactual',
            new_name='otrosdatos',
        ),
        migrations.RenameField(
            model_name='historiasclinica',
            old_name='motivoconsulta',
            new_name='tratamiento',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='abd',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='autorizacion',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='comonosconocio',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='contrato',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='cuotamod',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='eps',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='escolaridad',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='fc',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='fr',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='imc',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='nombreAcompañante',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='ocupacion',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='parentescoAcompañante',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='parentescoResponsable',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='peso',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='pin',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='profesion',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='responsableApellidosAcompañante',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='responsableNombresAcompañante',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='superficiecorporal',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='ta',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='talla',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='telefonoAcompañante',
        ),
        migrations.RemoveField(
            model_name='historiasclinica',
            name='temperatura',
        ),
    ]
