import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import myapp.routing


os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'Routing_Django_Channels.settings')

application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'wesocket': URLRouter(
        myapp.routing.websocket_urlspatterns()
    )
})
