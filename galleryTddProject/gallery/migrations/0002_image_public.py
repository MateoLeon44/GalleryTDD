# Generated by Django 2.2.4 on 2020-03-30 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]