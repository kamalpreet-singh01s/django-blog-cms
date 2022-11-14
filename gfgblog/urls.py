from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# customizing admin interface
admin.site.site_header = 'GeeksForGeeks'
admin.site.site_title = 'GeeksForGeeks'
admin.site.index_title = 'GeeksForGeeks Administration'

urlpatterns = [
    # urls handling admin route
    path('admin/', admin.site.urls),
    # urls handling blog routes
    path('', include('blog.urls')),
    # urls handling WYSIWYG editor
    path('editor/', include('django_summernote.urls')),
]

# add condition in django urls file
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
