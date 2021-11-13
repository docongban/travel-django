"""tour URL Configuration

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
from home import views
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="trang chu"),
    path('home/about',views.about,name="gioi thieu"),
    path('home/contact',views.contact,name="lien lac"),
    path('home/tour',views.tour,name="tour"),
    path('home/productcat/<int:id>',views.productcat,name="tour theo nuoc"),
    path('home/productdetail/<int:id>',views.productdetail,name="chi tiet tour"),
    path('summernote/', include('django_summernote.urls')),
    path('home/message_ok',views.message,name="message_ok"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)