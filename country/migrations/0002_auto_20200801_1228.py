# Generated by Django 2.2.6 on 2020-08-01 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('country', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='domain',
            new_name='topLevelDomain',
        ),
    ]
