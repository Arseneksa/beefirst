# Generated by Django 3.0.5 on 2020-06-20 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('create_cv', '0006_auto_20200606_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='cvfolder',
            name='m_infoperso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='create_cv.Infoperso'),
        ),
    ]