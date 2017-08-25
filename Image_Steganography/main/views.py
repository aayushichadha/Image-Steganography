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
import os
from django.utils.encoding import smart_str
from django.http import HttpResponse
from StringIO import StringIO
from django.contrib import messages
from django.shortcuts import render_to_response


def home(request):
    documents = Document.objects.all()
    return render(request, 'index.html', { 'documents': documents })


def encode(request):

    if request.method == 'POST' and request.FILES['image']:
            form = Document()
            form.Image = request.FILES['image']
            form.save()
            text = request.POST['data']
            img = Image.open(settings.MEDIA_ROOT + '/' + form.Image.name)
            encoded_file = "enc" + form.Image.name
            img_encoded = encode_image(img,text)

            if img_encoded:
                img_encoded.save(encoded_file)
                print "Message Encoded! "
                os.startfile(encoded_file)
                response = HttpResponse(content_type='application/force-download')
                response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(encoded_file)

            else:
                print "FAIL!!!!!"
            return redirect('home')

    else:
        print "FORM FAIL"
    return render(request, 'send.html')




def decode(request):

    if request.method == 'POST' and request.FILES['image']:
            form = Document()
            form.Image = request.FILES['image']
            form.save()
            img = Image.open(settings.MEDIA_ROOT + '/' + form.Image.name)
            hidden_text = decode_image(img)
            messages.info(request, 'The Secret Message is:'+hidden_text)
            print hidden_text
            msg= 'The Secret Message is:'+hidden_text
            return render(request, 'retrieve.html', {"message":msg})
    else:
         print "FORM FAIL"
         return render(request,'retrieve.html', {"message":''})
