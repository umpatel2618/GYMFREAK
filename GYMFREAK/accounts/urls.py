from django.urls import path
from . import views
from .views import index

urlpatterns = [
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
]
