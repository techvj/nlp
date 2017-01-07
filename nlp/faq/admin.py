from django.contrib import admin

# Register your models here.
from .models import Bot, QuestionAnswer

admin.site.register(Bot)

admin.site.register(QuestionAnswer)