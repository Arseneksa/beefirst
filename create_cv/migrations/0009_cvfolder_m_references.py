# Generated by Django 3.0.5 on 2020-06-20 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_cv', '0008_reference'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvfolder',
            name='m_references',
            field=models.ManyToManyField(blank=True, to='create_cv.Reference'),
        ),
    ]