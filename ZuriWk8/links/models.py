from django.db import models
from django.contrib.auth import get_user_model

from . import managers

# Create your models here.


class Link(models.Model):
	target_url = models.URLField(max_length=200)
	description = models.CharField(max_length=200)
	identifier = models.SlugField(blank=True, unique=True)
	author = get_user_model()
	created_date = models.DateTimeField()
	active = models.BooleanField(default=True)
	objects = models.Manager()
	public = managers.ActiveLinkManager()

	def __str__(self):
		return self.target_url
