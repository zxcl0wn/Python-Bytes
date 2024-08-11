from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # fields = '__all__'
    prepopulated_fields = {'slug': ("title",)}
