# Generated by Django 2.2.5 on 2019-10-23 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoManage', '0014_auto_20191017_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='优惠券使用',
            name='备注',
        ),
        migrations.RemoveField(
            model_name='入库记录',
            name='备注',
        ),
        migrations.RemoveField(
            model_name='出库记录',
            name='备注',
        ),
        migrations.RemoveField(
            model_name='学生',
            name='备注',
        ),
        migrations.RemoveField(
            model_name='班',
            name='备注',
        ),
        migrations.RemoveField(
            model_name='班级分配',
            name='备注',
        ),
        migrations.RemoveField(
            model_name='缴费',
            name='备注',
        ),
        migrations.RemoveField(
            model_name='老师',
            name='备注',
        ),
        migrations.RemoveField(
            model_name='课程表',
            name='备注',
        ),
        migrations.AlterField(
            model_name='备注',
            name='备注',
            field=models.TextField(blank=True),
        ),
    ]
