from django.urls import path
from .views import BotConfig, ParseConfig, ParseConfig2, BotDelete, BotEdit, start_bot, start_bot2, stop_bot, stop_all_tasks


urlpatterns = [
    path('', BotConfig.as_view(), name='botconfig'),
    path('parseconfig/', ParseConfig.as_view(), name='parseconfig'),
    path('parseconfig2/', ParseConfig2.as_view(), name='parseconfig2'),
    path('<int:pk>/botdelete/', BotDelete.as_view(), name='botdelete'),
    path('<int:pk>/botedit/', BotEdit.as_view(), name='botedit'),
    path('start_bot/', start_bot, name='start_bot'),
    path('start_bot2/', start_bot2, name='start_bot2'),
    path('stop_bot/', stop_bot, name='stop_bot'),
    path('stop_all_bots/', stop_all_tasks, name='stop_all_bots'),
]