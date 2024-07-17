from rest_framework import serializers
from .models import Machines

class MachinesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Machines
        fields= ['id','name','type','initiated_date']


