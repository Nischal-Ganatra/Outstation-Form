from django.db import models
from django.core.urlresolvers import reverse


class Info(models.Model):
    name = models.CharField(max_length=250)
    roomno = models.CharField(max_length=250)
    bitsid = models.CharField(max_length=250)
    destination = models.CharField(max_length=250)
    leavingdate = models.DateField()
    returningdate = models.DateField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Outst:thankyou')


class Approved(models.Model):
    name = models.CharField(max_length=250)
    accepted = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Outst:thankyou')

