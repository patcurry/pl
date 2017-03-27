from django.db import models


class Pad(models.Model):
    name = models.CharField(max_length=20, unique=True, blank=False)
    status = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return str(self.name)

'''
class Locker(models.Model):
    name = models.CharField(max_length=12, unique=True, blank=True, null=True)
    pad = models.ManyToManyField(Pad)
    status = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        ordering = ('status')
'''
