# Generated by Django 3.2.3 on 2021-08-17 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=200)),
                ('sentence', models.CharField(max_length=500)),
                ('date', models.DateField()),
                ('title', models.FloatField()),
                ('date_m', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('twitter_id', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('twitter_user_url', models.CharField(max_length=500)),
                ('description', models.CharField(max_length=500)),
                ('user_created', models.DateField()),
                ('profile_img', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word_user_id', models.CharField(max_length=200)),
                ('text', models.CharField(max_length=200)),
                ('value', models.IntegerField()),
            ],
        ),
    ]