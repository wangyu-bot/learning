from django.conf.urls import url
from blog.views import *
from django.conf import settings
from blog.upload import upload_image

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r"^uploads/(?P<path>.*)$", "django.views.static.serve", {"document_root": settings.MEDIA_ROOT,}),
    url(r'^admin/upload/(?P<dir_name>[^/]+)$', upload_image, name='upload_image'),
    url(r'^archive$', archive, name='archive'),
    url(r'^biaoqian$', biaoqian, name='biaoqian'),
    url(r'^article/$', article, name='article'),
]
