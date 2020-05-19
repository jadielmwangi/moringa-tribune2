from django.contrib import admin

# Register your models here.
from .models import Editor,Article,tags

admin.site.register(Editor)
admin.site.register(Article)
admin.site.register(tags)