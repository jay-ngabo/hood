# Generated by Django 2.2.24 on 2022-01-03 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hoodapp', '0006_auto_20220103_1050'),
    ]

    operations = [
        migrations.RenameField(
            model_name='business',
            old_name='created_at',
            new_name='created_on',
        ),
        migrations.RenameField(
            model_name='business',
            old_name='updated_at',
            new_name='updated_on',
        ),
    ]
