from rest_framework import serializers

# from api.models import Coder


# write your serializers 

class CoderSerializer(serializers.Serializer):
    id=serializers.IntegerField()
    name=serializers.CharField(max_length=255)
    domain=serializers.CharField(max_length=100)
    company=serializers.CharField(max_length=100)
    salary=serializers.IntegerField()

                                                                                                                                                                                 


                                                                                                                                                                                    
