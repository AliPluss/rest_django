from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *

# create post model
# Create get all data in:------- start the get -> function 
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_postes(request):
    try:
      postes = Post.objects.all()
    except Post.DesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = PostSerializer(postes,many=True)
    return Response(serializer.data)
#        ---end get all post--- 

# Create new post data :-----start the post -> function 
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_post(request):
    if request.method == 'POST':
       try:
        serializer = PostSerializer(data=request.data)
       except PostSerializer.DesNotExist:
           return Response(status=status.HTTP_400_BAD_REQUEST) 
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#           ---end the post new function---

#create get one by id:--- start the get one date -> function
@api_view(['GET'])
def get_one_post(request, pk):
    try:
        post =Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)   
    serializer = PostSerializer(post)
    return Response(serializer.data, status=status.HTTP_200_OK)     
#       --- end the get one date function ---

#create update the opst:-- start the put -> function
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_post(request,pk):
    try:
        post = Post.objects.get(pk=pk)

    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
       serializer = PostSerializer(post,data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_200_OK)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#             --- end the update date ---    
    

#create update the opst:--- start the delete -> function    
@api_view(['DELETE'])
def delete_post(request,pk):
    try:
        post = Post.objects.get(pk=pk)

    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'DELETE':
            post.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
#            --- end the delete date ---
#--------------------------------------------------------------- end the post



 
