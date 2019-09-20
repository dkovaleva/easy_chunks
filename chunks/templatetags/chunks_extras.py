from django import template
from django.template.defaultfilters import register
from django.utils import translation
from django.utils.html import format_html
from django.urls import reverse
from chunks.models import Chunk

register = template.Library()

class ChunkNode(template.base.Node):

    def __init__(self, name, lang):
        self.name = name
        self.lang = lang

    def render(self, context):
        chunk, created = Chunk.objects.get_or_create(
                name=self.name, lang=self.lang
            )
        url = reverse('chunks:edit_chunk', args=[chunk.pk])
        if chunk.text:
            text = chunk.text
        else:
            text = "Add some text here"
        return format_html("<span id='chunk_id_%s'>%s</span><span chunk_id='%s' url='%s' class='badge chunk-badge badge-success'>Edit</span>" % (chunk.pk, text, chunk.pk, url))

@register.tag
def chunk(parser, token):
    try:
        chunk_name = token.contents.split()[1]
    except (IndexError, ValueError):
        raise template.TemplateSyntaxError("%r tag requires arguments" % token.contents.split()[0])
    lang = translation.get_language()
    return ChunkNode(chunk_name, lang)