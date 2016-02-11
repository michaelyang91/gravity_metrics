from __future__ import unicode_literals
import datetime
from django.db import models


class Device(models.Model):
	device = models.IntegerField()

	def __str__(self):
		return '%s' % self.device

	def save(self, *args, **kwargs):
		device = self.device
		super (Device, self).save(*args, **kwargs)

class Delta(models.Model):
	timestamp = models.IntegerField() # How to convert UNIX to Human-friendly?
	delta = models.IntegerField(default=0)
	device = models.ForeignKey(Device)

	def __str__(self):		
		return 'DEVICE ID: %s | DELTA: %s @ TIME: %s' % (self.device, self.delta, self.timestamp)

	def save(self, *args, **kwargs):
		device = self.device
		timestamp = self.timestamp
		delta = self.delta
		super (Delta, self).save(*args, **kwargs)
