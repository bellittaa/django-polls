from time import timezone
from django.db import models
from django.contrib.auth import get_user_model
user = get_user_model()
import datetime 
from django.utils import timezone
from django.core.exceptions import ValidationError



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

    def save(self, user, *args, **kwargs):
        question_user = QuestionUser.objects.filter(user=user, question=self.question).count()
        if question_user > 0:
            raise ValidationError('Não é permitido votar mais de uma vez')

        question_user = QuestionUser.objects.create(user=user, question=self.question)
        question_user.save(*args, **kwargs)


class QuestionUser(models.Model):
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
