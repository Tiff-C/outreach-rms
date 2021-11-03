# Generated by Django 3.2.8 on 2021-11-03 13:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('address_1', models.CharField(max_length=128, verbose_name='Address line 1')),
                ('address_2', models.CharField(blank=True, max_length=128, verbose_name='Address line 2')),
                ('postcode', models.CharField(max_length=12, verbose_name='Postcode')),
                ('contact', models.CharField(blank=True, max_length=70, verbose_name='Main Contact Name')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Contact Phone')),
                ('email', models.EmailField(blank=True, max_length=320, verbose_name='Contact Email')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('school', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='schools.school')),
            ],
        ),
    ]
