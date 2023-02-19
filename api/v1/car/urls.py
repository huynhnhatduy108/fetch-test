from django.urls import path
from . import views

urlpatterns = [
    path('list', views.CarView.as_view({'get': 'get_list_car'}), name="get_list_car"),
    path('list_car_by_brand/<int:pk>', views.CarView.as_view({'get': 'get_list_car_by_brand'}), name="get_list_car_by_brand"),
    path('info/<int:pk>', views.CarView.as_view({'get': 'get_info'}), name="get_info"),
    path('create', views.CarView.as_view({'post': 'create_car'}),name="create_car" ),
    path('update/<int:pk>', views.CarView.as_view({'put': 'update_car'}),name="update_car"),
    path('delete/<int:pk>', views.CarView.as_view({'delete': 'delete_car'}),name="delete_car"),

]