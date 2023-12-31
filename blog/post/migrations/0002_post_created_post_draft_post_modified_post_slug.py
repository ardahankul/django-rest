# Generated by Django 4.2.3 on 2023-07-18 03:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 3, 2, 2, 717429, tzinfo=datetime.timezone.utc), editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='modified',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 18, 3, 2, 36, 873119, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=datetime.datetime(2023, 7, 18, 3, 2, 40, 413064, tzinfo=datetime.timezone.utc), editable=False, max_length=120, unique=True),
            preserve_default=False,
        ),
    ]
