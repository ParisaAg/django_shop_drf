from django.urls import path,include
from . import views




app_name = "accounts"


urlpatterns = [
    path('login/',views.LoginView.as_view(),name="login"),
# path("register/",views.login.as_view(),name="register"),
    path("logout/",views.LogOutView.as_view(),name="logout"),
]
