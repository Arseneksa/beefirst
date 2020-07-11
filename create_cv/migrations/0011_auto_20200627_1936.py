# Generated by Django 3.0.5 on 2020-06-27 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('create_cv', '0010_infoperso_m_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='infoperso',
            name='m_user_avatar',
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_user_avatar', models.ImageField(blank=True, upload_to='media/createcv')),
                ('m_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
