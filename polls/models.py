from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Question(models.Model):
	question_text = models.CharField(max_length=255)
	question_description = models.CharField(max_length=255, default='Basic Description')
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.question_text
# ------------------ QUESTION MODEL EXAMPLE ----------------------- #
	# 1)  'Are you happy about django'                     "June 16, 09:58 WAT"
	# 2)  'Are you...'  								   "June 15, 12:00 WAT"


class Choices(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE)
	choice_answer = models.CharField(max_length=20)
	votes = models.PositiveIntegerField(default=0)

	def __str__(self):
		return f"{self.question} ---> {self.choice_answer}"
# -------------------- CHOICES MODEL SAMPLE ------------------------------ #
	# 1) 'Are you happy about django'                     (Yes)/(No)            (1)/(3)
