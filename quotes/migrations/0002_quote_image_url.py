# Generated by Django 5.1.1 on 2024-09-15 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='image_url',
            field=models.URLField(blank=True),
        ),
    ]
