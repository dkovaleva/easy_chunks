# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from django.conf.urls.i18n import i18n_patterns
from index.views import main_page

urlpatterns = [
    path('admin/', admin.site.urls),
    #url(r'^chunks/', include('chunks.urls', namespace='chunks')),
]

urlpatterns += i18n_patterns(
    url(r'^$', main_page, name='main_page'),
    url(r'^chunks/', include('chunks.urls', namespace='chunks')),
)