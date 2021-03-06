# Generated by Django 4.0.4 on 2022-06-05 20:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('faculty_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['-faculty_name'],
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('group_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='asking.faculty')),
            ],
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('institute_name', models.CharField(max_length=30, primary_key=True, serialize=False)),
            ],
            options={
                'ordering': ['-institute_name'],
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('pk_mailing', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('mailing_date', models.DateField()),
                ('status', models.CharField(blank=True, choices=[('a', 'Active'), ('i', 'Inactive')], default='i', max_length=1)),
                ('institute', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='asking.institute')),
            ],
            options={
                'ordering': ['-mailing_date'],
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('pk_question', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular question', primary_key=True, serialize=False)),
                ('question', models.TextField(help_text='Enter a question', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_file', models.FileField(upload_to='')),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('file_checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('pk_student', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.CharField(blank=True, choices=[('s', 'Study'), ('g', 'Graduate')], default='s', max_length=1)),
                ('mail', models.CharField(max_length=50)),
                ('graduate_year', models.DateField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='asking.group')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('pk_result', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('graduate_number', models.IntegerField()),
                ('answer_number', models.IntegerField()),
                ('causes', models.IntegerField()),
                ('coefficient', models.FloatField()),
                ('employed', models.IntegerField()),
                ('graduate_year', models.DateField()),
                ('mailing', models.ManyToManyField(to='asking.mailing')),
            ],
            options={
                'ordering': ['pk_result'],
            },
        ),
        migrations.AddField(
            model_name='mailing',
            name='question',
            field=models.ManyToManyField(to='asking.question'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='asking.institute'),
        ),
    ]
