# Generated by Django 4.2.7 on 2024-10-18 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerStatistics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goals', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('appearances', models.IntegerField()),
                ('player', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='players.player')),
            ],
        ),
    ]
