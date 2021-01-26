from django.views.static import serve
from django.conf.urls import include, url
from django.contrib import admin
from memedata import views
from django.urls import path
from memedata.views import LoginView,LogoutView

from django.views import static
from django.conf import settings


urlpatterns = [
    # Examples:
    # url(r'^$', 'meme.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}, name='static'),
    # url(r'^index/$', views.index),  # 添加index/路径
    # url(r'^test/$', views.test),
    url(r'^api/v1/register/$', views.register),
    url(r'^regsiter_handler', views.regsiter_handler),
    url(r'^api/v1/login/$', LoginView.as_view()),
    url(r'^api/v1/testuser/$', views.test_user),
    url(r'^api/v1/teststar/$', views.test_star),
    url(r'^api/v1/identity/$', views.user_identity_auth),
    url(r'^api/v1/pk/$', views.multi_pk),
    url(r'^api/v1/logout/$',LogoutView.as_view()),
    url(r'^api/v1/upload',views.upload),
    url(r'^api/v1/test',views.test)
]
