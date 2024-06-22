from django.contrib import admin
from .models import Post, Person, Friendship

admin.site.register(Person)
admin.site.register(Post)
admin.site.register(Friendship)
