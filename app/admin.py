from django.contrib import admin
from .models import *



class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','descrption', 'is_public')
    list_display_links = ('id','title','descrption')
    list_per_page = 2
    list_editable = ('is_public',)
    # list_filter = ('',)
    # inlines = [
    #     Inline,
    # ]
    # raw_id_fields = ('',)
    # readonly_fields = ('',)
    # search_fields = ('title',)
    # date_hierarchy = ''
    # ordering = ('',)

# Register your models here..
admin.site.register(Category)
admin.site.register(Post,PostAdmin)
admin.site.register(PostComment)
admin.site.register(NestedComment)


