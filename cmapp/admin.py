from django.contrib import admin
from .models import Question, Answer, Comment

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['content']

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, CommentAdmin)
admin.site.register(Comment, CommentAdmin)

# Register your models here.
