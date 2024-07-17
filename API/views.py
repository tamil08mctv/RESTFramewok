from django.shortcuts import render
from rest_framework import generics,status
from .models import Machines
from rest_framework.response import Response
from .serializers import MachinesSerializer

# Create your views here.
class MachinesListCreate(generics.ListCreateAPIView):
    queryset = Machines.objects.all()
    serializer_class= MachinesSerializer

    def delete(self,request,*args,**kwargs):
        Machines.objects.all.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)                                                            

class MachinesRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset=Machines.objects.all()
    serializer_class= MachinesSerializer
    lookup_field="id"