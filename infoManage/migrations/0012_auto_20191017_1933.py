# Generated by Django 2.2.5 on 2019-10-17 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoManage', '0011_auto_20191017_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='优惠券',
            name='优惠券介绍',
            field=models.TextField(),
        ),
    ]
