from django.shortcuts import render
from django.http import HttpResponse
# import models 
from .models import Coder

# import serializers 
from .serializers import CoderSerializer

# for converting serializers into json 
from rest_framework.renderers import JSONRenderer

# from api import serializers

# Create your views here.

def coder_details(request,pk):
    # get the model data
    # coder = Coder.objects.all()
    coder = Coder.objects.get(id=pk)

    # print(coder)
    # convert model into serializers

    # serializer = CoderSerializer(coder,many=True)
    serializer = CoderSerializer(coder)

    # print(serializer)
    # print(serializer.data)

    # convert serializer into the json using JSONRenderer

    json_Data=JSONRenderer().render(serializer.data)
    # print(json_Data)

    return HttpResponse(json_Data,content_type='application/json')


