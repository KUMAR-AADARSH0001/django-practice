from rest_django.quickstart import views
from rest_framework import routers
from django.urls import include, path
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('snippets/', include("snippets.urls")),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("chat/", include("chat.urls"))
]
