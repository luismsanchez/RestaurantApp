# Generated by Django 3.2.8 on 2021-10-22 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0003_auto_20211021_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='product_descripcion',
            field=models.TextField(default='', verbose_name='Descripcion'),
        ),
        migrations.AddField(
            model_name='producto',
            name='product_valoracion',
            field=models.IntegerField(default=5, verbose_name='Valoracion'),
        ),
    ]
