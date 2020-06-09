from django.urls import path
from rest_framework_simplejwt import views as jwt_views
from . import views

urlpatterns = [
    path("api/config/", views.GetConfig.as_view(), name="get_config"),
    path("api/users/", views.UserCreate.as_view(), name="users"),
    path(
        "api/token/obtain/",
        jwt_views.TokenObtainPairView.as_view(),
        name="token_create",
    ),
    path(
        "api/token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"
    ),
    path("api/login/", views.Login.as_view(), name="login"),
    path("api/login/kiosk/", views.LoginKiosk.as_view(), name="login_kiosk"),
    path("api/password/reset/", views.api_reset_password, name="api_reset_password"),
    path("api/logout/", views.Logout, name="api_logout"),
    path("api/profile/", views.ProfileDetail.as_view(), name="api_profile"),
    path("api/profile/password/", views.api_password, name="api_password"),
    path("api/profile/idtoken/", views.api_digital_id, name="api_digital_id"),
    path("api/kiosks/", views.Kiosks.as_view(), name="api_kiosks"),
    path(
        "api/sitesessions/signin/", views.SiteSignIn.as_view(), name="api_site_sign_in"
    ),
    path(
        "api/sitesessions/signout/",
        views.SiteSignOut.as_view(),
        name="api_site_sign_out",
    ),
    path(
        "api/sitesessions/check/",
        views.UserSiteSession.as_view(),
        name="api_user_site_session",
    ),
    path("api/statistics/", views.Statistics.as_view(), name="api_statistics",),
    path("api/kiosks/<int:id>/", views.Kiosks.as_view(), name="api_kiosks"),
]
