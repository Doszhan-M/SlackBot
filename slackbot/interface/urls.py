from django.urls import path
from .views import BotConfig, start_bot, ParseConfig, stop_bot, stop_all_bots


urlpatterns = [
    path('', BotConfig.as_view(), name='botconfig'),
    path('parseconfig/', ParseConfig.as_view(), name='parseconfig'),
    path('start_bot/', start_bot, name='start_bot'),
    path('stop_bot/', stop_bot, name='stop_bot'),
    path('stop_all_bots/', stop_all_bots, name='stop_all_bots'),
]