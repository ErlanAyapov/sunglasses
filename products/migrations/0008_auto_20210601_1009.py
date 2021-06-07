# Generated by Django 3.2.3 on 2021-06-01 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_remove_order_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='buying_type',
            field=models.CharField(choices=[('Самовывоз', 'Самовывоз'), ('Доставка', 'Доставка')], default='Самовывоз', max_length=100, verbose_name='Тип заказа'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Новый заказ', 'Новый заказ'), ('Заказ в обработке', 'Заказ в обработке'), ('Заказ готов', 'Заказ готов'), ('Заказ выполнен', 'Заказ выполнен')], default='Новый заказ', max_length=100, verbose_name='Статус заказ'),
        ),
    ]
