# Generated by Django 4.2.7 on 2024-01-29 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submissions',
            name='linked_in',
        ),
        migrations.RemoveField(
            model_name='submissions',
            name='youtube',
        ),
    ]