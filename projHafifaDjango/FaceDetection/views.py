import os

from django.shortcuts import render
from .forms import UploadFileForm
from .minioClient import upload
from urllib3 import PoolManager
from .usefulFunctions import random_name


def face_detection(request):
    upload_name = random_name(15)
    result = ''
    if request.method == 'POST':
        image_form = UploadFileForm(request.POST, request.FILES)
        if image_form.is_valid():
            upload(request.FILES['image'], upload_name)
            http_request = PoolManager()
            response = http_request.request('GET', 'http://%s:5000/pred/%s/%s' % (os.environ['FLASK_IP'], 'images', upload_name))
            result = response.data.decode('utf-8')
    else:
        image_form = UploadFileForm()
    return render(request, 'FaceDetection/imageForm.html', {'form': image_form, 'result': result})