from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializer import *



# create the like and dislike:-------------------------------------- start the like    
@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def like_dislike_post(request,pk):
    try:
        blog = Post.objects.get(pk=pk)
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    user = request.user
    if user not in blog.likes.all(): 
        blog.likes.add(user)
    else:   
        blog.likes.remove(user)
    blog.update_like_counts()
    serializer = PostSerializer(blog)
    return Response(serializer.data)
                
#--------------------------------------------------------------- end the like