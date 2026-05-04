from django.urls import path,include,re_path
from . import views




app_name = "shop"


urlpatterns = [
    path('cart/',views.ShopProductListView.as_view(),name="products-list"),


]