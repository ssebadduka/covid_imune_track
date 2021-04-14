"""immune_track URL Configuration

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
from django.urls import path,include


# from app.views. import manage_details ,index_page
from app.views import personal_detail_view as personal_detail_view
# from app.views import manage_details as manage_details
# from app.urls.personal_view import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    
      
]