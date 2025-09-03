from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as nviews

urlpatterns = [
    path("", nviews.index, name="index"),
    path("novel/<int:novel_id>/", nviews.novel_detail, name="novel_detail"),
    path("novel/<int:novel_id>/chapter/<int:number>/", nviews.chapter_detail, name="chapter_detail"),
    path("chapter/<int:id>/", nviews.chapter, name="chapter"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="/"), name="logout"),
    path("register/", nviews.register, name="register"),
]
