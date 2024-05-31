from django.contrib import admin
from .models import PLanguage, Question, Answer, Comment, Information

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

class AnswerAdmin(admin.ModelAdmin):
    search_fields = ['content']

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['content']

class PLanguageAdmin(admin.ModelAdmin):
    search_fields = ['content']

class InformationAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, CommentAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PLanguage, PLanguageAdmin)
admin.site.register(Information, InformationAdmin)
# Register your models here.
