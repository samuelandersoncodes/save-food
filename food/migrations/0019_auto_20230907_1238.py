# Generated by Django 3.2.20 on 2023-09-07 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0018_auto_20230831_1236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='address',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='post',
            name='item_description',
            field=models.TextField(max_length=50),
        ),
    ]