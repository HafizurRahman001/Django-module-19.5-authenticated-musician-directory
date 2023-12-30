from django.shortcuts import render,redirect
from Album.forms  import AddAlbumForm
from Album.models import AddAlbum
from django.contrib import messages

# Create your views here.
def add_album(request):
    if request.method == 'POST':
        album_form = AddAlbumForm(request.POST)
        if album_form.is_valid():
            messages.success(request,"'ALBUM' Added Successfully")
            album_form.save()
            return redirect('add_album')
    else:
        album_form = AddAlbumForm()
    return render(request,'albumform.html',{'form':album_form})



def edit_album(request,id):
    post = AddAlbum.objects.get(pk = id)
    album_form = AddAlbumForm(instance=post)
    if request.method == 'POST':
        album_form = AddAlbumForm(request.POST, instance=post)
        if album_form.is_valid():
            album_form.save()
            messages.success(request,"Your 'ALBUM' Edited Successfully")
            return redirect('home')
    return render(request,'albumform.html',{'form':album_form})


def delete_album(request,id):
    post = AddAlbum.objects.get(pk=id)
    post.delete()
    return redirect('home')
