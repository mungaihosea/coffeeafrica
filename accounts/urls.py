from django.urls import path
from .views import homepage, profile, login, create_account, dashboard, GetFactoriesView, create_buyer_account, create_seller_account, logout

namespace = "accounts"

urlpatterns = [
    path("", homepage, name="homepage"),
    path("profile/", profile, name="profile"),
    path("login/", login, name="login"),
    path("dashboard/", dashboard, name="dashboard"),
    path("factories/", GetFactoriesView.as_view(), name="factories"),
    path('create_account/', create_account, name= "create_account"),
    path('create_buyer_account/', create_buyer_account, name = 'create_buyer_account'),
    path('create_seller_account/', create_seller_account, name = 'create_seller_account'),
    path("logout/", logout, name = "logout")
]
