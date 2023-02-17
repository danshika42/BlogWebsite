from django.urls import path
from .views import HomeBlogView

urlpatterns = [
    path('', HomeBlogView.as_view(),name='home'),
]
