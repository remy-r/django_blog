from django.contrib import admin
from .models import Status, Post, Category


admin.site.register(Post)
admin.site.register(Status)
admin.site.register(Category)

