# Generated by Django 4.1.3 on 2023-05-01 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imagine_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='imagemodel',
            old_name='image_url',
            new_name='image',
        ),
    ]
