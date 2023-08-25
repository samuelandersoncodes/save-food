# Generated by Django 3.2.20 on 2023-08-25 11:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0006_auto_20230825_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='reserved',
            field=models.ManyToManyField(blank=True, default='reserve', related_name='food_item_reserve', to=settings.AUTH_USER_MODEL),
        ),
    ]
