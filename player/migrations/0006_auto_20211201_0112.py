# Generated by Django 3.2.5 on 2021-11-30 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_rename_players_t20players'),
    ]

    operations = [
        migrations.AddField(
            model_name='t20players',
            name='ranking',
            field=models.CharField(default='N/A', max_length=10),
        ),
        migrations.AlterField(
            model_name='t20players',
            name='height',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
