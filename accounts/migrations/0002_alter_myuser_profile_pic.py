# Generated by Django 4.2.9 on 2024-02-09 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='profile_pic',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]
