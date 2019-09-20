from django.db import models

class Chunk(models.Model):
    name = models.CharField(null=False, blank=True, max_length=255)
    lang = models.CharField(null=False, blank=True, max_length=255)
    text = models.TextField(null=True, blank=True, default="")

    class Meta:
        unique_together = (('name', 'lang'),)
