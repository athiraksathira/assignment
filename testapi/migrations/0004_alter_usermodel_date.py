# Generated by Django 4.0.3 on 2022-04-23 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapi', '0003_alter_usermodel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usermodel',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]