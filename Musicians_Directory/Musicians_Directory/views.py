from django.shortcuts import render
from Album.models import AddAlbum


def home(request):
    display_data = AddAlbum.objects.all()
    print(display_data)
    return render(request,'display_data.html', {'allData':display_data})