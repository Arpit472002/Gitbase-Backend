# Generated by Django 4.2.9 on 2024-02-19 06:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('project', '0002_alter_project_project_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectaccess',
            name='project_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='project.project'),
        ),
        migrations.AlterField(
            model_name='projectaccess',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to=settings.AUTH_USER_MODEL),
        ),
    ]
