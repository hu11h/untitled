from django.urls import path,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

app_name = 'shop'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('market', views.market, name='market'),
    path('store', views.product2_list, name='product2_list'),
    path('add1', views.add1, name='add1'),
    path('', views.index, name='index'),
    path('xxx', views.xxx, name='xxx'),
    path('1', views.m1, name='1'),
    path('2', views.m2, name='2'),
    path('3', views.m3, name='3'),
    path('4', views.m4, name='4'),
    path('5', views.m5, name='5'),
    path('6', views.m6, name='6'),
    path('7', views.m7, name='7'),
    path('8', views.m8, name='8'),
    path('9', views.m9, name='9'),
    path('10', views.m10, name='10'),
    path('shop', views.product_list, name='product_list'),
    path('<slug:category_slug>/', views.product_list, name='product_list_by_category'),
    path('d/<int:id>/<slug:slug>/', views.product2_detail, name='product2_detail'),
    path('<int:id>/<slug:slug>/', views.product_detail, name='product_detail'),
    
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": settings.MEDIA_ROOT}),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)