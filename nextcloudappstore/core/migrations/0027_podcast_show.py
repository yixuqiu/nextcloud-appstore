# Generated by Django 4.2.6 on 2023-10-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_podcast_alter_appapireleaseapiscope_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='podcast',
            name='show',
            field=models.BooleanField(default=True, verbose_name='Show podcast'),
        ),
    ]
