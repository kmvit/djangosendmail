from django.contrib import admin
from django.urls import path, include
from rest_framework import routers


from core.views import ClientViewSet, MailingViewSet, MessageViewSet
from .yasg import urlpatterns as swagger


router = routers.DefaultRouter()
router.register(r'client-list', ClientViewSet)
router.register(r'message-list', MessageViewSet)
router.register(r'mailing-list', MailingViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include("rest_framework.urls", namespace="rest_framework")),
]

urlpatterns += swagger