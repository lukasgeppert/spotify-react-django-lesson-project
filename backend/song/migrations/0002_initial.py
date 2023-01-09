# Generated by Django 4.1.5 on 2023-01-09 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('song', '0001_initial'),
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artists',
            field=models.ManyToManyField(to='user.artist'),
        ),
        migrations.AddField(
            model_name='song',
            name='genres',
            field=models.ManyToManyField(to='song.genre'),
        ),
        migrations.AddField(
            model_name='song',
            name='playlists',
            field=models.ManyToManyField(to='song.playlist'),
        ),
        migrations.AddField(
            model_name='playlist',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.customer'),
        ),
    ]
