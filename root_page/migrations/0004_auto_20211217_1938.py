# Generated by Django 3.2.9 on 2021-12-17 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root_page', '0003_project_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='url',
        ),
        migrations.AddField(
            model_name='project',
            name='url_colab',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='url_github',
            field=models.URLField(blank=True),
        ),
    ]