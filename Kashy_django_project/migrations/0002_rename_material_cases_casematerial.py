# Generated by Django 4.1.7 on 2023-03-08 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Kashy_django_project', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cases',
            old_name='material',
            new_name='casematerial',
        ),
    ]
