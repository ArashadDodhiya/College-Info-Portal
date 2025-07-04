from django.shortcuts import render
from .models import *

def home(request):
    events = Event.objects.all().order_by('-date')
    circulars = Circular.objects.all().order_by('-created_at')
    forms = RegistrationForm.objects.all()
    clubs = Club.objects.all()
    workshops = Workshop.objects.all()
    achievements = Achievement.objects.all()
    gallery = GalleryItem.objects.all()
    downloads = DownloadableResource.objects.all()
    return render(request, 'main/home.html', {
        'events': events,
        'circulars': circulars,
        'forms': forms,
        'clubs': clubs,
        'workshops': workshops,
        'achievements': achievements,
        'gallery': gallery,
        'downloads': downloads,
    })
