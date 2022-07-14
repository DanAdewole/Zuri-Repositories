from django.contrib import admin

from .models import Question, Choices

# Register your models here.


class ChoiceInline(admin.TabularInline):
	model = Choices
	extra = 3


class QuestionAdmin(admin.ModelAdmin):
	# fields = ['pub_date', 'question_text', 'question_description']
	# fieldsets = [
	# 	(None, {'fields': ['question_text']}),
	# 	('Question Description', {'fields': ['question_description']}),
	# 	('Date information', {'fields': ['pub_date']}),
	# ]

	list_display = ('question_text', 'question_description', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date',]
	search_fields = ['question_text']
	inlines = [ChoiceInline]

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choices)