# Generated by Django 4.2.9 on 2024-02-19 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repository',
            name='repo_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
