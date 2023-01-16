# Generated by Django 4.1.1 on 2023-01-15 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_shop_shop_street_alter_shop_shop_began_work_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_house_num',
            field=models.CharField(blank=True, default='', max_length=70, null=True, verbose_name='Дом'),
        ),
        migrations.AddField(
            model_name='shop',
            name='shop_info',
            field=models.TextField(default=''),
        ),
    ]
