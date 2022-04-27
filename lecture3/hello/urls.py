

from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("bohdan", views.bohdan, name="bohdan"),
    path("<str:name>", views.greet, name="greet")

    

]
