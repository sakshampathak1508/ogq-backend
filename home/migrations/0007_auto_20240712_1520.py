# Generated by Django 3.2.25 on 2024-07-12 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20240712_1506'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportsoptions',
            name='event_type',
            field=models.CharField(choices=[('olympics', 'olympics'), ('paralympics', 'paralympics'), ('junior', 'junior')], default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='juniorathletes',
            name='sport',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='olympic',
            name='sport',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='olympicresultplayers',
            name='olympic_year',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paralympic',
            name='sport',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
