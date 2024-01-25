from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *


# crete categroy get all:---------------------------------- start the categroy
@api_view(['GET'])
def categroy_get_all(request):
    try: 
     categroy = Category.objects.all()
    except Category.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = CategorySerializer(categroy, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
#      --- end get all categroy date ---

#create get one categroy
@api_view(['GET'])
def get_one_categroy(request,pk):
    try:
        categroy_one = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CategorySerializer(categroy_one)
    return Response(serializer.data, status=status.HTTP_200_OK)
#       --- end get one categroy date ---

# create post new categroy:
@api_view(['POST'])
def create_categroy(request):
     if request.method == 'POST':
            try:
                serializer = CategorySerializer(data=request.data)
            except CategorySerializer.DesNotExist:
                return Response(status=status.HTTP_400_BAD_REQUEST) 
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#      --- end post new categroy date ---     
     

# update categroy
@api_view(['PUT'])
def update_categroy(request,pk):
    if request.method == 'PUT':
        try:
            categry = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = CategorySerializer(categry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)    
#        --- end the update one categroy date --- 

# create delete categroy:  
@api_view(['DELETE'])
def delete_categroy(request,pk):
    try:
        categroy = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        categroy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
#          --- end delete catgroy ---
#--------------------------------------------------------------- end the categroy