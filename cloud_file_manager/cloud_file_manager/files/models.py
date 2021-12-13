from django.db import models

# Create your models here.
class File(models.Model):
    filename = models.CharField(max_length=1024, null=False)
    file = models.FileField(max_length=1024, null=False)
    content_type = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
