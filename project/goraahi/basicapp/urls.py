from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views
app_name='basicapp'

urlpatterns = [
	path('index/',views.index,name="index"),
	path('train/ ',views.train,name="train"),
	path('bus/',views.flight,name="bus"),
	path('flight/',views.flight,name="flight"),
	path('stod/',views.flight,name="stod"),
	path('signin/',views.flight,name="signin"),
	path('result/',views.result,name="result"),
]
