# Generated by Django 4.2.7 on 2023-12-08 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_rename_fname_newuser_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='email',
            field=models.EmailField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='newuser',
            name='username',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
