from django.urls import path
from .views import CategoryListView,CategoryRetrieveView,CategoryCreateView,CategoryDeleteView,CategoryUpdateView,CreateCategoryView


urlpatterns=[
    path("",CategoryListView.as_view(),name='category-view'),
    path("create/",CreateCategoryView.as_view(),name='category-create'),
    path("<int:pk>/retrieve/",CategoryRetrieveView.as_view(),name='category-retrieve'),
    path("<int:pk>/update/",CategoryUpdateView.as_view(),name='category-update'),
    path("<int:pk>/delete/",CategoryDeleteView.as_view(),name='category-delete'),
]