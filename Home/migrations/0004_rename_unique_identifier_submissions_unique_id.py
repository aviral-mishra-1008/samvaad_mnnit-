# Generated by Django 4.2.7 on 2024-01-29 10:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_remove_submissions_linked_in_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='submissions',
            old_name='unique_identifier',
            new_name='unique_id',
        ),
    ]
