from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def topic_insertion(request):
    if request.method=='POST':
        topic=request.POST['tn']

        cto=Topic.objects.get_or_create(topic_name=topic)[0]
        cto.save()
        fbo=Topic.objects.get_or_create(topic_name=topic)[0]
        fbo.save()
        hto=Topic.objects.get_or_create(topic_name=topic)[0]
        hto.save()
        vbo=Topic.objects.get_or_create(topic_name=topic)[0]
        vbo.save()

        return HttpResponse("Insertion of topic model is done")



    return render(request,'topic_insertion.html')


def webpage_insertion(request):
    LTO=Topic.objects.all()
    d={'LTO':LTO}

    if request.method=='POST':
        tn=request.POST['tn']
        name=request.POST['ne']
        url=request.POST['ul']

        to=Topic.objects.get(topic_name=tn)
        WO=Webpage.objects.get_or_create(topic_name=to,name=name,url=url)[0]
        WO.save()

        return HttpResponse("Insertion of webpage model is done")





    return render(request,'webpage_insertion.html',d)


def multiple_webpages(request):
    TO=Topic.objects.all()
    d={'TO':TO}

    if request.method=='POST':
        msts=request.POST.getlist('tn')
        EWOS=Webpage.objects.none()
        for j in msts:
            EWOS=EWOS|Webpage.objects.filter(topic_name=j)
        d1={'EWOS':EWOS}

        return render(request,'display_webpages.html',d1)

                  
    return render(request,'multiple_webpages.html',d)


    