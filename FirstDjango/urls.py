
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('items', views.items, name="items-list"),
    path('item/<int:item_id>', views.item_info, name="item-info")
]
