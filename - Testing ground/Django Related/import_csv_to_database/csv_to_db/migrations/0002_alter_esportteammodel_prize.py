# Generated by Django 3.2.7 on 2021-10-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('csv_to_db', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='esportteammodel',
            name='prize',
            field=models.CharField(max_length=100),
        ),
    ]
