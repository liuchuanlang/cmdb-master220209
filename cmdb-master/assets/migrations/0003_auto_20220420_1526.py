# Generated by Django 3.1 on 2022-04-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0002_auto_20220418_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testinterface',
            name='testdata',
            field=models.CharField(max_length=3000, verbose_name='测试数据'),
        ),
    ]
