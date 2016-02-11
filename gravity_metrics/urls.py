"""gravity_metrics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from gravity_metrics.get_data import views, models

# admin / password!

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^get-data/$', views.get_data, name='get-data'),
    url(r'^by-time/$', views.order_by_time, name='order-by-time'),
    url(r'^by-device/$', views.order_by_device, name='order-by-device')

]
