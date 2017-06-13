from django.contrib import admin
from .models import Choice, Question, Person


class ChoiceInline(admin.StackedInline):
	model = Choice
	extra = 5

class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['question_text']}),
		('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	
class PersonAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields': ['first_name']}),
	]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Person, PersonAdmin)