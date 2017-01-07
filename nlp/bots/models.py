from django.db import models

# Create your models here.
class Bot(models.Model):
    bot_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
    	return self.bot_name


class Task(models.Model):
    bot_name = models.ForeignKey(Bot)
    task = models.CharField(max_length=200)

    def __str__(self):
    	return self.task


class Utterance(models.Model):
	task = models.ForeignKey(Task)
	utterance = models.CharField(max_length=400, default="")

	def __str__(self):
		return self.utterance


class CustomEntity(models.Model):
    bot_name = models.ForeignKey(Bot)
    sentence = models.CharField(max_length=400,default="")
    entity = models.CharField(max_length=100,default="")
    entity_type = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.entity + " - " + self.entity_type