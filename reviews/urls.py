from django.urls import path
from . import views

urlpatterns = [
    path('review/', views.ReviewCreateListView.as_view(), name='review-create-list'),
    path('review/<int:pk>/', views.ReviewRetrieveUpdateDestroyViewModel.as_view(), name='review-detail-view'),
]
