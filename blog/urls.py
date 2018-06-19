"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from home.views import home_view,menu_view,phrases_view,test_view,test_result_view,ranking_view,test_korean_view,test_turkish_view,test_english_view,test_spanish_view,menu_kr,menu_tk,menu_sp,phrases_kr,phrases_sp,phrases_tk
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    url(r'^$', home_view, name='home'),
    
    url(r'^menu/', menu_view, name='menu'),
    url(r'^menu_kr/', menu_kr, name='menu_kr'),
    url(r'^menu_sp/', menu_sp, name='menu_sp'),
    url(r'^menu_tk/', menu_tk, name='menu_tk'),
    
    url(r'^phrases$', phrases_view, name='phrases'),
    url(r'^phrases_kr$', phrases_kr, name='phrases_kr'),
    url(r'^phrases_sp$', phrases_sp, name='phrases_sp'),
    url(r'^phrases_tk$', phrases_tk, name='phrases_tk'),
    
    url(r'^test/', test_view, name='test'),
    url(r'^test-korean$', test_korean_view, name='test-korean'),
    url(r'^test-turkish$', test_turkish_view, name='test-turkish'),
    url(r'^test-english$', test_english_view, name='test-english'),
    url(r'^test-spanish$', test_spanish_view, name='test-spanish'),
    url(r'^test_result$', test_result_view, name='test_result'),
    url(r'^ranking$', ranking_view, name='ranking'),

    url(r'^post/', include('post.urls')),

    url(r'^admin/', admin.site.urls),
    
    url(r'^accounts/', include('accounts.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#URL for uploaded files