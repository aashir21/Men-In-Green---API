# Generated by Django 3.2.5 on 2021-12-13 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0003_auto_20211209_2132'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleWithImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Pakistan Cricket', max_length=200)),
                ('date_of_creation', models.CharField(default='DD/MM/YY', max_length=50)),
                ('body', models.TextField()),
                ('card_image', models.TextField(default='https://www.crictracker.com/wp-content/uploads/2018/10/PCB.jpg')),
                ('img_1', models.TextField(blank=True, default='https://www.crictracker.com/wp-content/uploads/2018/10/PCB.jpg')),
                ('img_2', models.TextField(blank=True, default='https://www.crictracker.com/wp-content/uploads/2018/10/PCB.jpg')),
                ('img_3', models.TextField(blank=True, default='https://www.crictracker.com/wp-content/uploads/2018/10/PCB.jpg')),
                ('img_4', models.TextField(blank=True, default='https://www.crictracker.com/wp-content/uploads/2018/10/PCB.jpg')),
            ],
        ),
    ]
