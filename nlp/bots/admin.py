from django.contrib import admin
admin.site.site_header = 'NLP Administration'
# Register your models here.
from .models import Bot, Task, Utterance, CustomEntity

admin.site.register(Bot)

admin.site.register(Task)

admin.site.register(Utterance)

admin.site.register(CustomEntity)