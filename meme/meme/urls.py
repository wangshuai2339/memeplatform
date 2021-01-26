from django.conf.urls import include, url
from django.contrib import admin
from memedata import views
from django.urls import path
from django.views import static
from django.conf import settings

urlpatterns = [
    # Examples:
    # url(r'^$', 'meme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^static/(?P<path>.*)$', static.serve,{'document_root': settings.STATIC_ROOT}, name='static'),
    url(r'^index/$', views.index),
    url(r'^admin/', admin.site.urls),
    url(r'^memedata/', include('memedata.urls')),  # 用户模块

]
handler404 = "memedata.views.page_not_found"
