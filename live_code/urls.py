from django.urls import path
from . import views

urlpatterns = [
    path('',views.main_page,name='main_page'),
    path('input_barang',views.input_barang,name='input_barang'),
    path('barang/<int:barang_id>/',views.barang_detail,name='barang_detail'),

]