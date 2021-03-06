# Generated by Django 2.0.6 on 2018-10-17 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20181011_1448'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bodega',
            name='ubicacion',
        ),
        migrations.AddField(
            model_name='bodega',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='fotos'),
        ),
        migrations.AlterField(
            model_name='aprendiz',
            name='identificacion',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='bodega',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='cuentadante',
            name='identificacion',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='ficha',
            name='numero_ficha',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='material',
            name='codigo_sena',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='programa',
            name='nombre',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
