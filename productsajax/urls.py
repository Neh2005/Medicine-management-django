from django.urls import path
from . import views

urlpatterns = [
    path('retrieve',views.list_products,name='list_products'),
    path('list_template',views.listtemplate,name='list_template'),
    path('create',views.create_products,name='create_products'),
    path('get_products',views.get_products, name='get_product'),
    path('update_products',views.update_products, name='update_product'),
    path('delete', views.delete_product, name='delete_product'),
    ]