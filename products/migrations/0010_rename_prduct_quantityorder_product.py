# Generated by Django 3.2.3 on 2021-06-01 15:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210601_2140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quantityorder',
            old_name='prduct',
            new_name='product',
        ),
    ]