from django.urls import path
from .views import CartCreateView,CartListView

urlpatterns=[
    path("",CartListView.as_view(),name="cart-view"),
    path("create/",CartCreateView.as_view(),name="cart-create"),
]