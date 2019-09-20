from django import forms
from chunks.models import Chunk


class ChunkForm(forms.ModelForm):
    class Meta:
         model = Chunk
         fields = ['text']