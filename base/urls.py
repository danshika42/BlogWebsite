from django.urls import path
from .views import HomeBlogView,PostDetailView,AddPostView,EditPostView,DeletePostView

urlpatterns = [
    path('', HomeBlogView.as_view(),name='home'),
    path('article/<int:pk>', PostDetailView.as_view(),name='article'),
    path('addpost/',AddPostView.as_view(),name='add-post'),
    path('editpost/<int:pk>',EditPostView.as_view(),name='edit-post'),
    path('deletepost/<int:pk>',DeletePostView.as_view(),name='delete-post'),
]
