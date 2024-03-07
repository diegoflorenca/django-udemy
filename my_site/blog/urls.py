from django.urls import path
from . import views

urlpatterns = [
    path("", views.StartingPageView.as_view(), name="starting-page"),
    path("posts/", views.AllPostsViews.as_view(), name="posts-page"),
    path("posts/comment/", views.AddCommentView.as_view(), name="add-comment"),
    path("posts/read-later/", views.ReadLaterView.as_view(), name="read-later"),
    # <slug:slug> is a path converter provided by Django
    path("posts/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page")
]
