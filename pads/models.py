from django.db import models


class Locker(models.Model):
    name = models.CharField(max_length=20, unique=True, blank=True, null=True)
    status = models.CharField(max_length=20, default='empty', blank=True, null=True)
    code = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return str(self.name)


class Pad(models.Model):
    name = models.CharField(max_length=20, unique=True, blank=False)
    status = models.CharField(max_length=20, blank=True, null=True)
    locker = models.ManyToManyField(Locker)

    def __str__(self):
        return str(self.name)


