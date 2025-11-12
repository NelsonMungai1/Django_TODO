# configurinf urls to the views within myapp
from django.urls import path
from . import views
urlpatterns=[
    path("Test",views.temp,name="Test"),
    path("home",views.home,name="Home")
]