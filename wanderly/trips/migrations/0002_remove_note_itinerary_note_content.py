# Generated by Django 5.1.3 on 2024-12-03 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='itinerary',
        ),
        migrations.AddField(
            model_name='note',
            name='content',
            field=models.TextField(default=1, max_length=71),
            preserve_default=False,
        ),
    ]
