# INTERNAL URLS BE CAREFUL WHEN EDITING
from django.conf.urls import url
from lingooWEBAPP import views
from django.urls import path, include

from .views import resultView, HomePageView, ResultPageView

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # url(r'get_article/$', views.get_article),
    path('get_article/', views.ResultPageView.as_view(), name='result'),    
 #   path('get_article/', resultView, name='result'),
    ]
