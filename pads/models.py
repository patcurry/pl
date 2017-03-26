from django.db import models


class Pad(models.Model):
    name = models.CharField(max_length=12, unique=True, blank=False)

    def __str__(self):
        return str(self.name)
