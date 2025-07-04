from django.db import models

class Event(models.Model):
    CATEGORY_CHOICES = [
        ('Academic', 'Academic'),
        ('Cultural', 'Cultural'),
        ('Workshop', 'Workshop'),
        ('Fest', 'Fest'),
        ('Sports', 'Sports'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='events/')
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    registration_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Circular(models.Model):
    TYPE_CHOICES = [
        ('Exam', 'Exam'),
        ('Fee', 'Fee'),
        ('Holiday', 'Holiday'),
        ('General', 'General'),
    ]
    title = models.CharField(max_length=200)
    description = models.TextField()
    file_upload = models.FileField(upload_to='circulars/')
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class RegistrationForm(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField()
    last_date = models.DateField()

    def __str__(self):
        return self.title

class Club(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clubs/')
    description = models.TextField()
    faculty_in_charge = models.CharField(max_length=100)
    latest_activity = models.TextField()

    def __str__(self):
        return self.name

class Workshop(models.Model):
    title = models.CharField(max_length=200)
    speaker = models.CharField(max_length=200)
    poster = models.ImageField(upload_to='workshops/')
    date = models.DateField()
    time = models.TimeField()
    venue = models.CharField(max_length=200)
    registration_link = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Achievement(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='achievements/')
    date = models.DateField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class GalleryItem(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='gallery/')
    event_name = models.CharField(max_length=200)
    date = models.DateField()

    def __str__(self):
        return self.title

class DownloadableResource(models.Model):
    CATEGORY_CHOICES = [
        ('Syllabus', 'Syllabus'),
        ('Handbook', 'Handbook'),
        ('Rules', 'Rules'),
        ('Timetable', 'Timetable'),
    ]
    title = models.CharField(max_length=200)
    file = models.FileField(upload_to='downloads/')
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES)

    def __str__(self):
        return self.title
