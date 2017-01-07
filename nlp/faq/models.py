from django.db import models

# Create your models here.
class Bot(models.Model):
    bot_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
    	return self.bot_name


class QuestionAnswer(models.Model):
    bot_name = models.ForeignKey(Bot)
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=400)

    def __str__(self):
    	return self.question