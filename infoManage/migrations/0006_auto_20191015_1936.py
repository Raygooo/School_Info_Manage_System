# Generated by Django 2.2.5 on 2019-10-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoManage', '0005_auto_20191015_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='学生',
            name='学生生日',
            field=models.DateField(),
        ),
    ]
