from django.urls import path
from .views import homepage, profile, login, create_account, dashboard, GetFactoriesView

namespace = "accounts"

urlpatterns = [
    path("", homepage, name="homepage"),
    path("profile/", profile, name="profile"),
    path("login/", login, name="login"),
    path("create_account/", create_account, name="create_account"),
    path("dashboard/", dashboard, name="dashboard"),
    path("factories/", GetFactoriesView.as_view(), name="factories"),
]
