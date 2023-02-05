# Generated by Django 3.2.17 on 2023-02-05 13:23

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=55)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=50)),
                ('Image', models.URLField(blank=True, max_length=255, null=True)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Capacity', models.IntegerField(blank=True, null=True)),
                ('Registration_onset', models.DateTimeField()),
                ('Registration_end', models.DateTimeField()),
                ('Event_onset', models.DateTimeField()),
                ('Event_end', models.DateTimeField()),
                ('Is_published', models.BooleanField(default=False)),
                ('Expired', models.BooleanField(default=False)),
                ('Published_data', models.DateTimeField()),
                ('Created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('Category', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='events.category')),
            ],
        ),
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50, unique_for_year=True)),
                ('Image', models.URLField(blank=True, max_length=255, null=True)),
                ('Resume_link', models.URLField(blank=True, max_length=255, null=True)),
                ('Bio', models.TextField(blank=True, null=True)),
                ('Available', models.BooleanField(default=True)),
                ('Created_date', models.DateTimeField(auto_now=True)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Registrations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Event_threshold', models.DurationField(default=datetime.timedelta(seconds=300))),
                ('Programs_threshold', models.DurationField(default=datetime.timedelta(seconds=300))),
                ('Created_date', models.DateTimeField(auto_now=True)),
                ('Updated_date', models.DateTimeField(auto_now_add=True)),
                ('Event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.events')),
            ],
        ),
        migrations.CreateModel(
            name='Event_programs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Topic', models.CharField(max_length=55)),
                ('Description', models.TextField(blank=True, null=True)),
                ('Session_link', models.URLField(blank=True, max_length=255, null=True)),
                ('Available', models.BooleanField(default=True)),
                ('Session_date', models.DateTimeField()),
                ('Created_date', models.DateTimeField(auto_now=True)),
                ('Updated_date', models.DateTimeField(auto_now_add=True)),
                ('Event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.events')),
                ('Lecturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.lecturer')),
            ],
        ),
    ]
