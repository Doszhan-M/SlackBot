from django.contrib import admin
from .models import Posts, SlackBots


class PostsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'public_time', 'link',)
    list_display_links = ('headline', 'public_time', 'link',)
    list_filter = ('headline', 'public_time',)
    search_fields = ('headline', 'public_time',)

class BotAdmin(admin.ModelAdmin):
    list_display = ('token', 'url', 'agent', 'host',)
    list_display_links = ('token', 'agent',)
    list_filter = ('token',)
    search_fields = ('token',)


admin.site.register(Posts, PostsAdmin)
admin.site.register(SlackBots, BotAdmin)

admin.site.site_title = 'SlackBot for SkillFactory'
admin.site.site_header = 'SlackBot for SkillFactory'