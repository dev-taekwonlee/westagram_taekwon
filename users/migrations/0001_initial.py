# Generated by Django 4.0.5 on 2022-06-12 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=20, unique=True)),
                ('date_of_birth', models.DateField()),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
