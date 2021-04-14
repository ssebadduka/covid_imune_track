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
from django.urls import path


from app.views import personal_detail_view as personal_detail_view
from app.views import account_view as account_view

admin.site.site_header = 'Covid Immunisation Tracking'
admin.site.index_title = 'Covid Immunisation Tracking'
admin.site.site_title = 'Covid Immunisation Tracking'



dashbord_url=[
    path('home/', personal_detail_view.index_page, name="index_page"),
   
    path('manage_details/', personal_detail_view.manage_details, name='manage_details'),
]

account_url = [
    path('', account_view.login, name="login"),
    path('login', account_view.login, name="login"),
    path('logout', account_view.logout, name="logout"),

    # path('manage_details/', personal_detail_view.manage_details,
    #      name='manage_details'),
]

urlpatterns = [ 
]+dashbord_url+account_url
