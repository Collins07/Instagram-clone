# Generated by Django 3.2.2 on 2022-06-05 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='DEFAULT VALUE', upload_to='profile_pics/'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='DEFAULT VALUE', upload_to='images/')),
                ('name', models.CharField(blank=True, max_length=250)),
                ('caption', models.CharField(blank=True, max_length=250)),
                ('date_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('profile', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='images', to='instagram.profile')),
            ],
        ),
    ]
