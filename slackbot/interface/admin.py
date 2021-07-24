from django.contrib import admin
from .models import Posts, SlackBots, TaskConfig


class PostsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'public_time', 'link', 'status',)
    list_display_links = ('headline', 'public_time', 'link', )
    list_filter = ('headline', 'public_time', 'status',)
    search_fields = ('headline', 'public_time', 'status',)


class BotAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_display_links = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)


admin.site.register(Posts, PostsAdmin)
admin.site.register(SlackBots, BotAdmin)
admin.site.register(TaskConfig)

admin.site.site_title = 'SlackBot for SkillFactory'
admin.site.site_header = 'SlackBot for SkillFactory'
