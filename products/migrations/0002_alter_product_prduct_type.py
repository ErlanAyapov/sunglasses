# Generated by Django 3.2.3 on 2021-05-29 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prduct_type',
            field=models.CharField(choices=[('all', 'Оптом'), ('one', 'Розница')], default='all', max_length=100, verbose_name='Тип заказа'),
        ),
    ]
