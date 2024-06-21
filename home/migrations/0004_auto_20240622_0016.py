# Generated by Django 3.2.25 on 2024-06-21 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20240615_1418'),
    ]

    operations = [
        migrations.CreateModel(
            name='AthleteStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_athletes', models.CharField(default='', max_length=20)),
                ('senior_athletes', models.CharField(default='', max_length=20)),
                ('junior_athletes', models.CharField(default='', max_length=20)),
                ('para_athletes', models.CharField(default='', max_length=20)),
            ],
            options={
                'verbose_name': 'Athlete Stats',
                'verbose_name_plural': 'Athlete Stats',
            },
        ),
        migrations.CreateModel(
            name='Countdown',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(default='', max_length=20)),
                ('content', models.TextField(blank=True)),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
            ],
            options={
                'verbose_name': 'Countdown',
                'verbose_name_plural': 'Countdown',
            },
        ),
        migrations.CreateModel(
            name='MedalStats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('olympics', models.CharField(default='', max_length=20)),
                ('world_championships', models.CharField(default='', max_length=20)),
                ('asian_games', models.CharField(default='', max_length=20)),
                ('commonwealth_games', models.CharField(default='', max_length=20)),
                ('youth_olympics', models.CharField(default='', max_length=20)),
                ('junior_world_championships', models.CharField(default='', max_length=20)),
                ('paralympics', models.CharField(default='', max_length=20)),
            ],
            options={
                'verbose_name': 'Medal Stats',
                'verbose_name_plural': 'Medal Stats',
            },
        ),
        migrations.RenameField(
            model_name='homepagecarousel',
            old_name='name',
            new_name='title',
        ),
        migrations.AddField(
            model_name='teamogqindia',
            name='about_them',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='teamogqus',
            name='about_them',
            field=models.TextField(blank=True),
        ),
    ]
