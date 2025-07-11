# Generated by Django 5.2.4 on 2025-07-02 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='achievements/')),
                ('date', models.DateField()),
                ('category', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Circular',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('file_upload', models.FileField(upload_to='circulars/')),
                ('type', models.CharField(choices=[('Exam', 'Exam'), ('Fee', 'Fee'), ('Holiday', 'Holiday'), ('General', 'General')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='clubs/')),
                ('description', models.TextField()),
                ('faculty_in_charge', models.CharField(max_length=100)),
                ('latest_activity', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='DownloadableResource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('file', models.FileField(upload_to='downloads/')),
                ('category', models.CharField(choices=[('Syllabus', 'Syllabus'), ('Handbook', 'Handbook'), ('Rules', 'Rules'), ('Timetable', 'Timetable')], max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='events/')),
                ('category', models.CharField(choices=[('Academic', 'Academic'), ('Cultural', 'Cultural'), ('Workshop', 'Workshop'), ('Fest', 'Fest'), ('Sports', 'Sports')], max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=200)),
                ('registration_link', models.URLField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='gallery/')),
                ('event_name', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('link', models.URLField()),
                ('last_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('speaker', models.CharField(max_length=200)),
                ('poster', models.ImageField(upload_to='workshops/')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('venue', models.CharField(max_length=200)),
                ('registration_link', models.URLField(blank=True)),
            ],
        ),
    ]
