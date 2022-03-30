from django.urls import path
from .views import viewHome, viewRead, viewDelete, viewCreate, viewUpdate, viewRegister, viewLoginUser, viewLogout,viewChangePass
urlpatterns =  [
    path("", viewHome, name = "home"),
    path("stock/<int:id>/", viewRead, name = "read"),
    path("delete-stock/<int:id>/", viewDelete, name = "delete"),
    path("add-stock/", viewCreate, name = "create"),
    path("update-stock/<int:id>/", viewUpdate, name = "update"),
    path('register-user', viewRegister, name="register-user"),
    path('login-user', viewLoginUser, name="login-user"),
    path('logout-user', viewLogout, name="logout-user"),
    path('change-pass/', viewChangePass, name="change-pass"),
]