# Generated by Django 5.1.3 on 2024-12-13 03:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('achvs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userachv',
            old_name='user_seq',
            new_name='user_ref',
        ),
    ]