"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('api/brand/', include('api.v1.brand.urls')),
    path('api/car/', include('api.v1.car.urls')),
]

api_url_v1_patterns = [
    path('api/brand/', include('api.v1.brand.urls')),
    path('api/car/', include('api.v1.car.urls')),

]

urlpatterns += [
    path('v1/schema/', SpectacularAPIView.as_view(urlconf=api_url_v1_patterns, api_version='v1'), name="schema_v1"),
    path('v1/' + "docs/", SpectacularSwaggerView.as_view(url_name="schema_v1"), name='swagger_v1'),
    path('v1/' + "redoc/", SpectacularRedocView.as_view(url_name="schema_v1"), name='redoc_v1')
]
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
