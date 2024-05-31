from django import forms
from .models import Question, Answer, Comment, Information

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'imgs', 'planguage']
        labels = {
            'subject': '제목',
            'content': '내용',
            'imgs': '이미지',
            'planguage': '언어',
        }

class InfoForm(forms.ModelForm):
    class Meta:
        model = Information
        fields = ['subject','content','imgs']
        labels = {
            'subject' : '제목',
            'content' : '내용',
            'imgs' : '이미지',
        }

class AnswerForm(forms.ModelForm):
    prefix = 'answer'
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class CommentForm(forms.ModelForm):
    prefix = 'comment'
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }