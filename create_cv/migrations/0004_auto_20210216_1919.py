# Generated by Django 3.0.5 on 2021-02-16 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create_cv', '0003_auto_20210216_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infoperso',
            name='m_telephone',
            field=models.IntegerField(blank=True, help_text='Numero de telephone', null=True),
        ),
    ]