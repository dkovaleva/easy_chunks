from django.conf.urls import url
from django.urls import re_path


from . import views

app_name = 'chunks'

urlpatterns = [
    re_path(r'^edit/(?P<chunk_id>\d+)/?$', views.EditChunkView.as_view(), name="edit_chunk")
]