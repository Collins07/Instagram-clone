# Generated by Django 3.2.2 on 2022-06-05 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0005_auto_20220605_1731'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-pk']},
        ),
    ]