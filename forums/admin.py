from django.contrib import admin

from forums.models import Category, Forum, Topic, Post


class ForumAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'position', 'is_closed')


admin.site.register(Category)
admin.site.register(Forum, ForumAdmin)
admin.site.register(Topic)
admin.site.register(Post)
