from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Images
# Create your views here.

import base64


def index(request):
    template = loader.get_template('imgstore/homepage.html')
    context = {}
    return HttpResponse(template.render(context,request))


def imagebox(request):

    if request.method=='GET':
        context = {}
        return render(request,'imgstore/error.html', context)
    
    byte_info = request.FILES['img_input'].file.read()
    image_type = request.FILES['img_input'].content_type[6:] #length of the word image is 6
    image_info = request.POST['img_caption']
    
    converted = base64.b64encode(byte_info)
    byte_in_str = str(converted.decode("utf-8"))
    img_src = "data:"+image_type+";base64,"+byte_in_str

    #save the 'new_image' to data base
    new_image = Images.objects.create(image_code=byte_info,caption=image_info,image_type=image_type)

    context = {
        'img_src':img_src
    }
    
    return render(request,'imgstore/store.html',context)

#used in form input
def store(request):

    store_length = len(Images.objects.all())
    image_shown = Images.objects.all()[store_length-1]

    image_list = Images.objects.all()
    print(type(image_list))
    #create an array of objects
    store = []

    for i in range (0, len(image_list)):
        img_id = image_list[i].id
        byte_info = image_list[i].image_code.tobytes()
        image_type = image_list[i].image_type
        converted = base64.b64encode(byte_info)
        byte_in_str = str(converted.decode("utf-8"))
        img_src = "data:"+image_type+";base64,"+byte_in_str
        img_caption = image_list[i].caption

        container = {
            'id':img_id,
            'img_src':img_src,
            'img_caption':img_caption
        }
        store.append(container)


    # byte_info = image_shown.image_code.tobytes()
    # image_type = image_shown.image_type

    # converted = base64.b64encode(byte_info)
    # byte_in_str = str(converted.decode("utf-8"))
    # img_src = "data:"+image_type+";base64,"+byte_in_str

    context = store
    return render(request,'imgstore/store.html',context)
    
