from django.urls import path
from .views import OrderCreateView,OrderDeleteView,OrderListView,OrderRetrieveView,OrderUpdateView,ProductPurchasedByBuyer,DeliveryCreateAPIView,DeliveryRetrieveUpdateDestroyAPIView,DeliveryListView

urlpatterns=[
    path("",OrderListView.as_view(),name='order-view'),
    path("create/",OrderCreateView.as_view(),name='order-create'),
    path("retrieve/<int:pk>/",OrderRetrieveView.as_view(),name='order-retrieve'),
    path("update/<int:pk>/",OrderUpdateView.as_view(),name='order-update'),
    path("delete/<int:pk>/",OrderDeleteView.as_view(),name='order-delete'),
    path("byuser/",ProductPurchasedByBuyer.as_view(),name='order-by-user'),
    
    path('delivery/create', DeliveryCreateAPIView.as_view(), name='delivery-create'),
    path('delivery/', DeliveryListView.as_view(), name='delivery-list'),
    path('delivery/<int:pk>/', DeliveryRetrieveUpdateDestroyAPIView.as_view(), name='delivery-detail'),

    
]