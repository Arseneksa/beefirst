# Generated by Django 3.0.5 on 2020-05-30 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_cv', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='diploma',
            name='m_intitule',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
