from django.db import models
from datetime import datetime

class Todo(models.Model):
    todo_title = models.CharField(max_length=100)
    todo_desc = models.TextField(max_length=500)
    date_created = models.DateTimeField(default=datetime.utcnow())