# Generated by Django 3.0.5 on 2020-06-20 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_cv', '0009_cvfolder_m_references'),
    ]

    operations = [
        migrations.AddField(
            model_name='infoperso',
            name='m_user_avatar',
            field=models.ImageField(blank=True, upload_to='media/createcv'),
        ),
    ]