import uuid
from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=500)
    artist = models.CharField(max_length=500, null=True)
    image = models.URLField(max_length=500)
    url = models.URLField(max_length=500, null=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.CharField(max_length=100, default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    class Meta:
        ordering = ['-created']
    
    def __str__(self):
        return self.title
    
