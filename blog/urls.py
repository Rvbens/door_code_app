from django.urls import path
from .views import home, HomeView, PostDetailView, PostUpdateView
from . import views

urlpatterns = [
    path('', home, name="blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name="post-update")
]