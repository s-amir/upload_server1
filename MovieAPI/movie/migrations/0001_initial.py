# Generated by Django 3.2.9 on 2021-11-28 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=450)),
                ('movie_genre', models.CharField(choices=[('comedy', 'Comedy'), ('action', 'Action'), ('animation', 'Animation'), ('horror', 'Horror'), ('science_fiction', 'Science')], max_length=30)),
                ('image_url', models.ImageField(upload_to='uploads/% Y/% m/% d/')),
                ('release_date', models.DateField(auto_now_add=True)),
                ('idbm_score', models.FloatField(default=8, max_length=10.0)),
            ],
        ),
    ]
