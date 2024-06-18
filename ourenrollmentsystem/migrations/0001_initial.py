# Generated by Django 5.0.6 on 2024-06-17 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('level_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('level', models.CharField(max_length=55)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'level',
            },
        ),
    ]
