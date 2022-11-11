import datetime

from unittest.util import _MAX_LENGTH
from django.db import models
from django.utils import timezone
from django.contrib import admin

# Create your models here.


class Question(models.Model):
	question_text = models.CharField(max_length=255)
	question_description = models.CharField(max_length=255, default='Basic Description')
	# pub_date = models.DateTimeField(auto_now_add=True)
	pub_date = models.DateTimeField('date published')

	def __str__(self):
		return self.question_text

	@admin.display(
		boolean=True,
		ordering='pub_date',
		description='Published recently?',
	)
	def was_published_recently(self):
		now = timezone.now()
		# return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
		return now - datetime.timedelta(days=1) <= self.pub_date <= now

# ------------------ QUESTION MODEL EXAMPLE ----------------------- #
	# 1)  'Are you happy about django'                     "June 16, 09:58 WAT"
	# 2)  'Are you...'  								   "June 15, 12:00 WAT"


class Choices(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_answer = models.CharField(max_length=200)
	votes = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"{self.question} ---> {self.choice_answer}"
# -------------------- CHOICES MODEL SAMPLE ------------------------------ #
	# 1) 'Are you happy about django'                     (Yes)/(No)            (1)/(3)
