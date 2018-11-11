from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter,  URLRouter
import k.routing


application = ProtocolTypeRouter({
     # (http->django views is added by default)
    'websocket': AuthMiddlewareStack(
        URLRouter(
            k.routing.websocket_urlpatterns
        )
    ),
})
