# Generated by Django 5.0.3 on 2024-03-10 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apiapp', '0002_userdata_alter_clients_created_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdata',
            name='password',
        ),
    ]
