from django.conf.urls import url
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator
import bloodapp.routing 
from bloodapp.consumers import NotifyConsumer

application = ProtocolTypeRouter({
    # (http->django views is added by default)
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter(
                [
                    #bloodapp.routing.websocket_urlpatterns
                    path('request/', NotifyConsumer),
                ]
            )
        )
    )
})
