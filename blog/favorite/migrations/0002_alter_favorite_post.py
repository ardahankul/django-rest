# Generated by Django 4.2.3 on 2023-08-08 13:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_modified_by_alter_post_user'),
        ('favorite', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorite',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='post.post'),
        ),
    ]