# Generated by Django 2.1.1 on 2018-09-17 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webshell', '0002_auto_20180917_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webshellinfo',
            name='envi_id',
            field=models.IntegerField(choices=[(1, '生产环境')], verbose_name='环境'),
        ),
    ]