from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *

   
#--------------------------------------------------------------- star the nested comment 
# create get all nested comment 
@api_view(['GET'])
def get_all_nested_comment(request):
    try: 
     nested_comment = NestedComment.objects.all()
    except Category.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = SerializerNestedComment(nested_comment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


# create get one nested comment 
@api_view(['GET'])
def get_nested_comment_one(request,pk):
    try:
        comment_one = NestedComment.objects.get(pk=pk)
    except NestedComment.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = SerializerNestedComment(comment_one)
    return Response(serializer.data , status=status.HTTP_200_OK)


# create new nested comment
@api_view(['POST'])
def create_nested_comment(request,pk):
    try:
        nested_comment = PostComment.objects.get(pk=pk)
    except PostComment.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        serializer = SerializerNestedComment(data=request.data)
        if serializer.is_valid():
            serializer.save(nested_comment=nested_comment)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    

# crate update nedted coment and delete 
@api_view(['PUT', 'DELETE'])
def update_and_delete_nested_coment(request,pk):
    try:
            nested_comment = NestedComment.objects.get(pk=pk)
    except NestedComment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PUT':
        serializer = SerializerNestedComment(nested_comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
  
    elif request.method == 'DELETE':
        nested_comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
#--------------------------------------------------------------- end the nested comment