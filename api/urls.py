"""
URL configuration for api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import re_path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from apps.core.views import HistoryViewSet, HistoryTwoViewSet, ContactServiceViewSet, OutlookServiceViewSet

router = DefaultRouter()
router.register(r'history', HistoryViewSet, basename='history')
router.register(r'history-two', HistoryTwoViewSet, basename='history-two')
router.register(r'contacts', ContactServiceViewSet, basename='contacts')

contacts_router = routers.NestedSimpleRouter(router, r'contacts',)
contacts_router.register(r'outlook', OutlookServiceViewSet,basename='outlook')

outlook_router = routers.NestedSimpleRouter(contacts_router, r'outlook')
outlook_router.register(r'outlook', OutlookServiceViewSet, basename='outlook')

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^', include(contacts_router.urls)),
    re_path(r'^', include(outlook_router.urls)),
]
