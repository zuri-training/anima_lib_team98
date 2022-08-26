from django.db import models
from django.contrib.auth.models import User

class SavedItems(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length = 200)
    code = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    updated = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.code

# Safe = False