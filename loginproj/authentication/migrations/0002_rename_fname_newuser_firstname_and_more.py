# Generated by Django 4.2.7 on 2023-12-07 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='newuser',
            old_name='fname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='newuser',
            old_name='lname',
            new_name='lastname',
        ),
    ]
