# Generated by Django 3.0.5 on 2020-07-01 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('create_cv', '0011_auto_20200627_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='m_user_avatar',
            field=models.ImageField(blank=True, upload_to='media/createcv/'),
        ),
        migrations.CreateModel(
            name='Langue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_nom', models.CharField(max_length=64)),
                ('m_niveau', models.CharField(max_length=64)),
                ('m_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]