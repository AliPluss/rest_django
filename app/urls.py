from  django.urls import path
from .comment import *
from .nested_comment import *
from .like_and_dislike import *
from .categroy import *
from .views import *

urlpatterns = [
    
    #------------------------------------------ start ->POST -> path:
    # urls get all date
    path('', get_all_postes),

    # urls app create new 
    path('create_post/', create_post),

    # urls app get one id = pk
    path('get_one/<int:pk>/', get_one_post),

    # urls app update post one id = pk
    path('update_post/<int:pk>/', update_post),

    # urls app delete id = pk
    path('delete_post/<int:pk>/', delete_post),
    ############################################

    #------------------------------------------ start -> CATEGROY -> path:
    # urls to get all the categroy data
    path('categroy/',categroy_get_all),

    # urls create new categroy
    path('create_categroy/',create_categroy),

    # urls get one categroy id = pk
    path('get_one_categroy/<int:pk>/',get_one_categroy),

    # urls update one categroy id = pk
    path('update_categroy/<int:pk>/',update_categroy),
    
    # urls delete one categroy id = pk
    path('delete_categroy/<int:pk>/',delete_categroy),
    #################################################

    #----------------------------------------- start -> COMMENT -> path:
    # urls create comment
    path('create_comment/<int:pk>/',create_comment),

    # urls get all comment
    path('comment_get_all',comment_get_all),

    # urls get one comment id = pk
    path('get_one_comment/<int:pk>/',get_one_comment),

    # urls update one comment id = pk
    path('update_coment/<int:pk>/',update_coment),

    # urls delete comment id = pk
    path('delete_comment/<int:pk>/',delete_comment),
    #################################################

   
    #-------------------------------------------- star nested  comment -> path
    #urls get all nested comment
    path('nested_comment/',get_all_nested_comment),

    #urls get one nested comment
    path('nested_comment_one/<int:pk>/',get_nested_comment_one),

    #urls create new nested comment py id = pk
    path('create_nested_comment/<int:pk>/',create_nested_comment),

    #urls update nested comment and delete py id = pk
    path('update_and_delete_nested_coment/<int:pk>/',update_and_delete_nested_coment),

    #################################################


    # ------------------------------------------ start -> LIKE -> path: 
    # urls like post id = pk
    path('like_dislike_post/<int:pk>/',like_dislike_post),
    ######################################################
   
]