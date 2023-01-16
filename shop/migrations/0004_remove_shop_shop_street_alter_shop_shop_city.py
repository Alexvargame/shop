# Generated by Django 4.1.1 on 2023-01-15 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_shop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='shop_street',
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_city',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.city', verbose_name='Город'),
        ),
    ]
