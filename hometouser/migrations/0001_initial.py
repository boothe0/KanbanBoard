# Generated by Django 5.2.1 on 2025-05-29 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('display_name', models.CharField(default='Guest', max_length=50)),
                ('password', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
