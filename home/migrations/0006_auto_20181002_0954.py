# Generated by Django 2.1.1 on 2018-10-02 14:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20181002_0952'),
    ]

    operations = [
        migrations.RenameField(
            model_name='material',
            old_name='nombre_material',
            new_name='nombre_materal',
        ),
    ]
