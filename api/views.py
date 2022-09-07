import io
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

# import models 
from .models import Coder

# import serializers 
from .serializers import CoderSerializer

# for converting serializers into json 
from rest_framework.renderers import JSONRenderer

from api import serializers

# from api import serializers

# Create your views here.

def coder_details(request,pk):
    # get the model data
    # coder = Coder.objects.all()
    coder = Coder.objects.get(id=pk)

    # print(coder)
    # convert model into serializers

    serializer = CoderSerializer(coder)

    # print(serializer)
    # print(serializer.data)

    # convert serializer into the json using JSONRenderer

    json_Data=JSONRenderer().render(serializer.data)
    # print(json_Data)

    return HttpResponse(json_Data,content_type='application/json')

    # when data is dict we dont need to specify the safe argument
    # return JsonResponse(serializer.data)


def coder_list(request):
    # get the model data
    coder = Coder.objects.all()

    # convert model into serializers

    serializer = CoderSerializer(coder,many=True)

    # convert serializer into the json using JSONRenderer
    
    json_Data = JSONRenderer().render(serializer.data)

    return HttpResponse(json_Data,content_type='application/json')

    # use JsonResponse to render the data 
                                                                                                                                                                                      
    # return JsonResponse(serializer.data,safe=False)


@csrf_exempt
def create_coder(request):

    if request.method =='POST':
        # get the client data
        json_data=request.body

        # convert json_data to stream 
        stream = io.BytesIO(json_data )

        # convert this stream to python data 

        data = JSONParser().parse(stream)

        # convert pythondata to complex data 
        serializer = CoderSerializer(data = data)

        # validation of serializers 

        if serializer.is_valid():
            serializer.save()
            response = {'msg':'Data created'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data,content_type='application/json')
            
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')






