from django.shortcuts import render,redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from forms import DocumentForm
from django.core.files.storage import FileSystemStorage
from models import Document
from forms import DocumentForm
from Encode import encode_image,decode_image
from PIL import Image
from django.core.files.base import ContentFile
import os.path
from StringIO import StringIO

def home(request):
    documents = Document.objects.all()
    return render(request, 'index.html', { 'documents': documents })


def simple_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        form.save()
        img = Image.open(Document.document)
        img_encoded = encode_image(img,"HEy ssup")
        if img_encoded:
                hidden_text = decode_image(img_encoded)
                print hidden_text



    return render(request, 'send.html')


def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'core/model_form_upload.html', {
        'form': form
    })