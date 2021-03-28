from django.urls import path
from .views import Test, test_action


urlpatterns = [
    path('', Test.as_view(), name='test'),
    path('test/', test_action, name='test_action'),
]