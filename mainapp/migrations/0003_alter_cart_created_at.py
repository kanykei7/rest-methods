# Generated by Django 4.1.1 on 2022-10-03 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_cartproduct_cart_alter_cartproduct_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
