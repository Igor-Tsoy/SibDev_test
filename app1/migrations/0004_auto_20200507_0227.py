# Generated by Django 3.0.6 on 2020-05-06 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200506_1822'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='deal',
            options={'ordering': ['customer']},
        ),
        migrations.RemoveField(
            model_name='deal',
            name='date',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='quantity',
        ),
    ]