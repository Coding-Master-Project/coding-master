from django.db import models
from django.contrib.auth.models import User

# class Img(models.Model):
#     img = models.ImageField(null=True, blank=True)

class PLanguage(models.Model):
    content = models.CharField(max_length=50)

    def __str__(self):
        return self.content

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question') #추천인
    views = models.PositiveIntegerField(default=0) #조회수
    imgs = models.ImageField(null=True, upload_to="", blank=True) #첨부파일 이미지
    planguage = models.ForeignKey(PLanguage, on_delete=models.CASCADE) # 프로그래밍 언어
    
    def __str__(self):
        return self.subject

class Information(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_information')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_information') #추천인
    views = models.PositiveIntegerField(default=0) #조회수
    imgs = models.ImageField(null=True, upload_to="", blank=True) #첨부파일 이미지
    planguage = models.ForeignKey(PLanguage, on_delete=models.CASCADE) # 프로그래밍 언어
    
    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer') #추천인

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_comment')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    information = models.ForeignKey(Information, on_delete=models.CASCADE,null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE, null=True)
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, related_name='recomment')
    content = models.TextField(max_length=200)
    create_date = models.DateTimeField()