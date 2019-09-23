import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView

from chunks.models import Chunk
from chunks.forms import ChunkForm

class EditChunkView(TemplateView):
    template_name = 'chunk_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.chunk_id = kwargs.get('chunk_id', 1)
        self.instance = get_object_or_404(Chunk, pk=self.chunk_id)
        self.request = request
        return super(EditChunkView, self).dispatch(request, *args, **kwargs)


    def get_context_data(self, *args, **kwargs):
        context = super(EditChunkView, self).get_context_data(*args, **kwargs)
        context['form'] = ChunkForm(instance=self.instance)
        return context

    def post(self, *args, **kwargs):
        data = {'result': 'fail'}
        form = ChunkForm(self.request.POST, instance=self.instance)
        if form.is_valid():
            try:
                form.save(commit=True)
                data['result'] = 'ok'
                data['text'] = form.instance.text
            except Exception as e:
                data['error_text'] = str(e)
        else:
            data['error_text'] = 'Please, fill in form correctly'
            data['errors'] = form.errors
        return HttpResponse(json.dumps(data), content_type='application/json')
