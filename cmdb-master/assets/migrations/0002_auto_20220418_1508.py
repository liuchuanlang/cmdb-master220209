# Generated by Django 3.1 on 2022-04-18 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testinterface',
            name='interfaceurl',
            field=models.CharField(max_length=200, unique=True, verbose_name='接口地址'),
        ),
    ]
