# Generated by Django 4.2.7 on 2024-10-18 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0004_remove_player_stats_player_assists_player_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='value',
            field=models.DecimalField(decimal_places=2, max_digits=14),
        ),
    ]
