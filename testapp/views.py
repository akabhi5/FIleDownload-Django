from django.shortcuts import render
from django.http import HttpResponse, FileResponse

def download_view(request):
    return FileResponse(open('image.jpg', 'rb'))