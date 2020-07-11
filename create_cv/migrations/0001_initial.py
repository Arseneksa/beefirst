# Generated by Django 3.0.5 on 2020-05-09 09:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_competence', models.CharField(max_length=64)),
                ('m_date', models.DateTimeField(auto_now=True, null=True)),
                ('m_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Loisir',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_loisir', models.CharField(max_length=64)),
                ('m_date', models.DateTimeField(auto_now=True, null=True)),
                ('m_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_etablissement', models.CharField(max_length=64)),
                ('m_tasks', models.TextField(blank=True, max_length=256, null=True)),
                ('m_start', models.DateField(blank=True, null=True)),
                ('m_end', models.DateField(blank=True, null=True)),
                ('m_date', models.DateTimeField(auto_now=True, null=True)),
                ('m_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Diploma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_diploma', models.CharField(max_length=64)),
                ('m_school', models.CharField(blank=True, max_length=64, null=True)),
                ('m_year', models.IntegerField(blank=True, null=True)),
                ('m_mention', models.CharField(blank=True, max_length=64, null=True)),
                ('m_date', models.DateTimeField(auto_now=True, null=True)),
                ('m_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CVFolder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_date', models.DateTimeField(auto_now=True, null=True)),
                ('m_competences', models.ManyToManyField(blank=True, to='create_cv.Competence')),
                ('m_diplomas', models.ManyToManyField(blank=True, to='create_cv.Diploma')),
                ('m_experiences', models.ManyToManyField(blank=True, to='create_cv.Experience')),
                ('m_loisirs', models.ManyToManyField(blank=True, to='create_cv.Loisir')),
                ('m_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Biographie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_description', models.TextField(max_length=256)),
                ('m_date', models.DateTimeField(auto_now=True, null=True)),
                ('m_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]