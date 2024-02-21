from django.urls import path
from . import views


urlpatterns = [
    path("", views.ReviewView.as_view(), name="index"),
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("review-detail/<int:id>", views.ReviewDetail.as_view(), name="review-detail")
]
