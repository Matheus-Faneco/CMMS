# Generated by Django 5.2.3 on 2025-06-27 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MaintenanceWorker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('worker_name', models.CharField(max_length=16)),
                ('worker_role', models.CharField(default='Técnico', max_length=50)),
            ],
        ),
    ]
