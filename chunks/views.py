import json

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from chunks.models import Chunk
from chunks.forms import ChunkForm

def edit_chunk(request, chunk_id):
    chunk = get_object_or_404(Chunk, pk=chunk_id)
    if request.method == 'GET':
        form = ChunkForm(instance=chunk)
        return render(request, 'chunk_form.html', {'form': form})
    if request.method == 'POST':
        print(request.POST)
        data = {'result': 'fail'}
        form = ChunkForm(request.POST, instance=chunk)
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

