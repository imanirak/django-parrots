# Generated by Django 4.0.3 on 2022-04-13 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_parrotsnacks'),
    ]

    operations = [
        migrations.AddField(
            model_name='parrot',
            name='parrotsnacks',
            field=models.ManyToManyField(to='main_app.parrotsnacks'),
        ),
    ]
