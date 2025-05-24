from reviews.models import Review
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from reviews.serializers import ReviewModelSerializer


class ReviewCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer


class ReviewRetrieveUpdateDestroyViewModel(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Review.objects.all()
    serializer_class = ReviewModelSerializer