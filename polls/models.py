from time import timezone
from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()
import datetime 
from django.utils import timezone



class Question(models.Model):
    question_text = models.CharField(max_length=300)
    pub_date = models.DateTimeField("date published", default=timezone.now)
    author = models.ForeignKey(
        user, editable = False, on_delete=models.DO_NOTHING, null=True
    )

    def was_published_recently(self):
        return self.pub_date >=timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=300)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
