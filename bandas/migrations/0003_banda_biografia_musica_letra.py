# Generated by Django 4.0.6 on 2024-06-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bandas', '0002_rename_link_spotify_musica_link_alter_album_capa_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='banda',
            name='biografia',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='musica',
            name='letra',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
