from django.contrib import admin
from .models import Post, Author, Tag


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_filter = ("date_created", "author", "tags")
    list_display = ("title", "author", "date_created")


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)
