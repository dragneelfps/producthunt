from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from . import api

urlpatterns = [
    path('create', views.create, name='create'),
    path('<int:product_id>', views.detail, name='detail'),
    path('<int:product_id>/upvote', views.upvote, name='upvote'),

    # function based views
    # path('api', api.product_list, name='api_product_list'),
    # path('api/<int:pk>', api.product_detail, name='api_product_detail'), 

    # class based views
    # path('api', api.ProductView.as_view(), name='api_product_list'),
    # path('api/<int:pk>', api.ProductDetailView.as_view(), name='api_product_detail'), 

    # mixins
    # path('api', api.ProductList2.as_view(), name='api_product_list'),
    # path('api/<int:pk>', api.ProductDetailView2.as_view(), name='api_product_detail'), 

    # generic
    path('api', api.ProductList3.as_view(), name='api_product_list'),
    path('api/<int:pk>', api.ProductDetailView3.as_view(), name='api_product_detail'), 
]

urlpatterns = format_suffix_patterns(urlpatterns)