from django.urls import path


from .consumers import TestConsumer

ws_urlpatterns = [
    path('user/<int:pk>/', TestConsumer.as_asgi())
]