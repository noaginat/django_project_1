# Generated by Django 4.0 on 2022-02-14 16:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_thumb'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='review',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
    ]