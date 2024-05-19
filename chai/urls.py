from django.urls import path,include # type: ignore
from . import views

urlpatterns = [
    path('', views.all_chai,name='all_chai'),
]
