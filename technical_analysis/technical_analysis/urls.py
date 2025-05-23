"""
URL configuration for technical_analysis project.

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
from django.contrib import admin
from django.urls import path
from technical_analysis_app import views
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create_view),
    path('list', views.list_view),
    path('detail/<id>', views.detail_view),
    path('update/<id>',views.update_view),
    path('api/', include('technical_analysis_app.urls')),


    # path('', include("apis.urls")),
    # path('api-auth/', include('rest_framework.urls')),
]


