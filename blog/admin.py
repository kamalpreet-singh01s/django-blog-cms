# importing admin and posts model
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Posts


# creating admin class
class BlogAdmin(SummernoteModelAdmin):
    # displaying posts with title slug and created time
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    # prepopulating slug from title
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


# registering admin class
admin.site.register(Posts, BlogAdmin)
