# Generated by Django 3.2.5 on 2021-12-02 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='title',
            field=models.CharField(default='Pakistan Cricket', max_length=200),
        ),
    ]
