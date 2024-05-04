from django.urls import path
from .views import LoginView,LogoutView,Signup,UserListView,UserDeleteView,UserRetrieveView,UserUpdateView

urlpatterns=[
    path("",UserListView.as_view(),name="user-view"),
    path("<int:pk>/",UserRetrieveView.as_view(),name="user-retrieve"),
    path("<int:pk>/delete/",UserDeleteView.as_view(),name="user-delete"),    
    path("<int:pk>/update/",UserUpdateView.as_view(),name="user-update"),
    path("signup/",Signup.as_view(),name="signup"),


    path("login/",LoginView.as_view(),name="login"),
    path("logout/",LogoutView.as_view(),name="logout"),
]