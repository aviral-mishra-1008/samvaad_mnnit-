# Generated by Django 4.1.5 on 2023-03-12 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vyas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='unique_identifier',
            field=models.IntegerField(default=0, null=True),
        ),
    ]