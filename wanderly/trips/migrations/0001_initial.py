# Generated by Django 5.1.3 on 2024-12-07 19:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=21)),
                ('description', models.TextField(max_length=51)),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('location', models.CharField(blank=True, max_length=51, null=True)),
                ('category', models.CharField(choices=[('Sightseeing', 'Sightseeing'), ('Dining', 'Dining'), ('Adventure', 'Adventure'), ('Relaxation', 'Relaxation'), ('Shopping', 'Shopping')])),
                ('itinerary', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='activities', to='trips.itinerary')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=21)),
                ('description', models.TextField(blank=True, max_length=51, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_published', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('General', 'General'), ('Packing', 'Packing'), ('Reminder', 'Reminder'), ('Feedback', 'Feedback')])),
                ('content', models.TextField(max_length=71)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notes', to=settings.AUTH_USER_MODEL)),
                ('trip', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='trips.trip')),
            ],
        ),
        migrations.AddField(
            model_name='itinerary',
            name='trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itineraries', to='trips.trip'),
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Food & Dining', 'Food & Dining'), ('Transport', 'Transport'), ('Accommodation', 'Accommodation'), ('Entertainment', 'Entertainment'), ('Shopping', 'Shopping'), ('Other', 'Other')])),
                ('description', models.TextField(blank=True, max_length=51, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='expenses', to='trips.trip')),
            ],
        ),
    ]
