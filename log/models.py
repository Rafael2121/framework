from sqlite3 import Timestamp
from django.db import models


class Log(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=5)
    raw_content = models.TextField()
