from rest_framework import serializers
from .models import *

# create serializer her:

# selializer post:--------------- start model serializer for post
class PostSerializer(serializers.ModelSerializer):
    # her for disply auther 
    auther = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post #--> transformation model post to json
        fields = '__all__' #--> disply all model post 
#-------------------------------------- end model serializer       
         

# selializer post commen to disply the content for post and auther:--> start model serializer for comment    
class PostCommentSerializer(serializers.ModelSerializer):
    # disply to read only
    post = serializers.StringRelatedField(read_only=True)
    # disply to read only
    auther = serializers.ReadOnlyField(source='auther.username') 

    class Meta:
        model = PostComment #--> transformation model post to json
        fields = '__all__' #--> disply all model comment
#-------------------------------------- end model serializer 
        
        
#---------------------------------- serializer nested comment models start
class SerializerNestedComment(serializers.ModelSerializer):
    auther = serializers.ReadOnlyField(source='auther.username')
    nested_comment = PostCommentSerializer(read_only= True)
    class Meta:
        model=NestedComment
        fields='__all__'

#-------------------------------- end the serializer nested comment


# selializer category :------------------------- start model serialser for categroy      
class CategorySerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    categroy_name = serializers.CharField()

    # to get all post belong to this category
    category = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category   #--> transformation model categroy to json
        fields = '__all__' #--> disply all model categroy
#---------------------------------------------- end model serializer categroy        