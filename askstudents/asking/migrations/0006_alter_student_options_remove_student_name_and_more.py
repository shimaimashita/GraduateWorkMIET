# Generated by Django 4.0.4 on 2022-06-01 08:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('asking', '0005_remove_questionmailing_mailing_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.RemoveField(
            model_name='student',
            name='patronymic',
        ),
        migrations.RemoveField(
            model_name='student',
            name='surname',
        ),
    ]