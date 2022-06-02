# Generated by Django 4.0.4 on 2022-05-19 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asking', '0004_faculty_group_institute_mailing_mailingresult_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionmailing',
            name='mailing',
        ),
        migrations.RemoveField(
            model_name='questionmailing',
            name='question',
        ),
        migrations.AddField(
            model_name='mailing',
            name='question',
            field=models.ManyToManyField(to='asking.question'),
        ),
        migrations.AddField(
            model_name='result',
            name='mailing',
            field=models.ManyToManyField(to='asking.mailing'),
        ),
        migrations.DeleteModel(
            name='MailingResult',
        ),
        migrations.DeleteModel(
            name='QuestionMailing',
        ),
    ]