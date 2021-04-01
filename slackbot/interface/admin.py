from django.contrib import admin
from .models import Posts, SlackBots, TaskConfig


class PostsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'public_time', 'link', 'status',)
    list_display_links = ('headline', 'public_time', 'link', )
    list_filter = ('headline', 'public_time', 'status',)
    search_fields = ('headline', 'public_time', 'status',)


class BotAdmin(admin.ModelAdmin):
    list_display = ('token',)
    list_display_links = ('token',)
    list_filter = ('token',)
    search_fields = ('token',)


admin.site.register(Posts, PostsAdmin)
admin.site.register(SlackBots, BotAdmin)
admin.site.register(TaskConfig)

admin.site.site_title = 'SlackBot for SkillFactory'
admin.site.site_header = 'SlackBot for SkillFactory'
