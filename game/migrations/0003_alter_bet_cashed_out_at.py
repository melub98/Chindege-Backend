# Generated by Django 5.2.1 on 2025-05-13 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_bet_cashed_out_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bet',
            name='cashed_out_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
