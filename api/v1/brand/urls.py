from django.urls import path

from . import views

urlpatterns = [
    path('list', views.BrandView.as_view({'get': 'get_list_brand'}), name="get_list_brand"),
    path('info/<int:pk>', views.BrandView.as_view({'get': 'get_info'}), name="get_info"),
    path('create', views.BrandView.as_view({'post': 'create_brand'}),name="create_brand" ),
    path('update/<int:pk>', views.BrandView.as_view({'put': 'update_brand'}),name="update_brand"),
    path('delete/<int:pk>', views.BrandView.as_view({'delete': 'delete_brand'}),name="delete_brand"),
]