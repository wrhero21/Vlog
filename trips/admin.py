from django.contrib import admin
from .models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id','title','created_at')
    list_filter = ('title',)
    search_fields = ('title',)
    ordering = ('id',)