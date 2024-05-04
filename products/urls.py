from django.urls import path
from .views import ProductListView,ProductCreateView,ProductRetrieveview,ProductDeleteView,ProductUpdateView,ProductByCategory,ReviewListCreateAPIView,ReviewRetrieveUpdateDestroyAPIView

urlpatterns=[
    path("",ProductListView.as_view(),name='product-view'),
    path("create/",ProductCreateView.as_view(),name='product-create'),
    path("<int:pk>/retrieve/",ProductRetrieveview.as_view(),name='product-retrieve'),
    path("<int:pk>/update/",ProductUpdateView.as_view(),name='product-update'),
    path("<int:pk>/delete/",ProductDeleteView.as_view(),name='product-delete'),
    path("category/<str:name>/",ProductByCategory.as_view(),name="category"),
    path('products/<int:product_id>/reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('reviews/<int:pk>/', ReviewRetrieveUpdateDestroyAPIView.as_view(), name='review-retrieve-update-destroy'),

]