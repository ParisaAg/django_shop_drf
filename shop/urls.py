from django.urls import path,include,re_path
from . import views




app_name = "shop"


urlpatterns = [
    path('product/list/',views.ShopProductListView.as_view(),name="products-list"),
    re_path(r"product/(?P<slug>[-\w]+)/detail/",views.ShopProductDetailView.as_view(),name="products-detail"),


]