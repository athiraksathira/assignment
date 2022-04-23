# Generated by Django 4.0.3 on 2022-04-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, unique=True)),
                ('date', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('income', models.PositiveIntegerField()),
                ('ipaddress', models.PositiveIntegerField()),
            ],
        ),
    ]
