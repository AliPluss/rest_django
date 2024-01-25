from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *


# creat get all commet:--------------------------------------- start the comment
@api_view(['GET'])
def comment_get_all(request):
    try: 
     categroy = PostComment.objects.all()
    except Category.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serializer = PostCommentSerializer(categroy, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
#       --- end the get all comment date ---

# create get one comment
@api_view(['GET'])
def get_one_comment(request,pk):
    try:
        comment_one = Post.objects.get(pk=pk)

    except PostComment.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    comment = PostComment.objects.filter(post=comment_one)
    serializer = PostCommentSerializer(comment, many=True)
    return Response(serializer.data , status=status.HTTP_200_OK)
#       --- end the get one comment date ---  
    
             
# creat new post commet            
@api_view(['POST'])
def create_comment(request,pk):
    try:
        post = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'POST':
        serializer = PostCommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=post)
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
#         --- end the post new comment date ---

# create update one comment
@api_view(['PUT'])
def update_coment(request,pk):
    if request.method == 'PUT':
        try:
            postComment = PostComment.objects.get(pk=pk)
        except PostComment.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        serializer = PostCommentSerializer(postComment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
#         --- end the update comment ---
    
# create delete one comment
@api_view(['DELETE'])
def delete_comment(request,pk):
    try:
        deletComment = PostComment.objects.get(pk=pk)
    except PostComment.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        deletComment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    
#         --- end the delete one  comment --- 
#--------------------------------------------------------------- end the comment