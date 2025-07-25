# Generated by Django 5.2.3 on 2025-06-27 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=30)),
                ('status', models.CharField(choices=[('O', 'Operational'), ('S', 'Stopped'), ('M', 'Maintenance')], default='Operational', max_length=20)),
            ],
        ),
    ]
