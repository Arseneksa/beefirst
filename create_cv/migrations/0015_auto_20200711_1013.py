# Generated by Django 3.0.5 on 2020-07-11 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('create_cv', '0014_auto_20200711_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='biographie',
            name='m_aide',
        ),
        migrations.RemoveField(
            model_name='competence',
            name='m_aide',
        ),
        migrations.RemoveField(
            model_name='cvfolder',
            name='m_aide',
        ),
        migrations.RemoveField(
            model_name='diploma',
            name='m_aide',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='m_aide',
        ),
        migrations.RemoveField(
            model_name='infoperso',
            name='m_aide',
        ),
        migrations.RemoveField(
            model_name='langue',
            name='m_aide',
        ),
        migrations.RemoveField(
            model_name='loisir',
            name='m_aide',
        ),
        migrations.RemoveField(
            model_name='reference',
            name='m_aide',
        ),
    ]
