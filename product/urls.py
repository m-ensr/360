from django.urls import path
from .views import (
    ProductHomeView,
    ProductDetailGenelView,
    ProductDetailNotlarView,
    ProductDetailSmmView,
    ProductDetailKaliteView,
    ProductDetailKampanyaView,
    ProductDetailHareketView,
    ProductAddNewView,
    ProductKategoriView,
    ProductSuppliersView,
    ProductSmmExpensesView,
)

urlpatterns = [
    path('', ProductHomeView.as_view(), name='product_home'),
    path('yeni-urun/', ProductAddNewView.as_view(), name='product_add_new'),
    path('kategori/', ProductKategoriView.as_view(), name='product_kategori'),
    path('tedarikciler/', ProductSuppliersView.as_view(), name='product_suppliers'),
    path('detay/genel/', ProductDetailGenelView.as_view(), name='product_detail_genel'),
    path('detay/notlar/', ProductDetailNotlarView.as_view(), name='product_detail_notlar'),
    path('detay/smm/', ProductDetailSmmView.as_view(), name='product_detail_smm'),
    path('detay/kalite/', ProductDetailKaliteView.as_view(), name='product_detail_kalite'),
    path('detay/kampanya/', ProductDetailKampanyaView.as_view(), name='product_detail_kampanya'),
    path('detay/hareket/', ProductDetailHareketView.as_view(), name='product_detail_hareket'),
    path('smm-yillik-giderler/', ProductSmmExpensesView.as_view(), name='smm_expenses'),


]
