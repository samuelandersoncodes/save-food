# Generated by Django 3.2.20 on 2023-08-28 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_auto_20230825_1654'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='reserve',
        ),
        migrations.AddField(
            model_name='post',
            name='reserved',
            field=models.BooleanField(default=False),
        ),
    ]
