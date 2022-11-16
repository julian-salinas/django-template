"""backend URL Configuration

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
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

# Docs description - Swagger - OpenAPI
description = f""""
<h1>Backend API</h1>
<p> Here you can find the documentation of the API. </p>
"""

schema_view = get_schema_view(
    openapi.Info(
        title="Backend API",
        default_version='1.0.0',
        description=description,
        contact=openapi.Contact(email="info@mail.com"),
        license=openapi.License(name="Here you have to put your email"),
    ),
    public=True,
    permission_classes= [],
    authentication_classes= [],
    url = "http://0.0.0.0:8000"
)

urlpatterns = [
    # django adminer page
    path('admin/', admin.site.urls),

    # api-docs
    path('api-docs/swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api-docs/redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # application urls
    path('api/', include('users.urls')),
]