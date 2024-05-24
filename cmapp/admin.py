from django.contrib import admin
from .models import Question, Comment

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['content']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Comment, CommentAdmin)

# Register your models here.
