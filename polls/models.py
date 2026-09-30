from time import timezone

from django.contrib import admin
from django.db import models
from django.db.models.deletion import CASCADE


class Question(models.Model):


            question_title = models.CharField(max_length=200, default="Nameless")
            question_text = models.CharField(max_length=200)
            pub_date = models.DateTimeField('date published',auto_now_add=True)

            def __str__(self):
                return self.question_text


            @admin.display(
                boolean = True,
                ordering= '-pub_date',
            )
            def is_too_small(self):
                if self.question_text.__len__() < 10:
                    return True
                else:
                    return False


class Choice(models.Model):
            question = models.ForeignKey(Question, on_delete=CASCADE)
            choice_text = models.CharField(max_length=200)
            votes = models.IntegerField(default=0)


            def __str__(self):
                return self.choice_text