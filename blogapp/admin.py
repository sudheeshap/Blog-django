from blogapp.models import *
from django.contrib import admin
class PostAdmin(admin.ModelAdmin):
    search_fields = ["title"]
    prepopulated_fields = {'slug': ('title',)}

class CommentAdmin(admin.ModelAdmin):
    display_fields = ["post", "author", "created"]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
