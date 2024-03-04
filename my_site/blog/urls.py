from django.urls import path
from . import views

urlpatterns = [
    path("", views.starting_page, name="starting-page"),
    path("posts/", views.posts, name="posts-page"),
    path("posts/comment/", views.AddCommentView.as_view(), name="add-comment"),
    path("posts/read-later/", views.ReadLaterView.as_view(), name="read-later"),
    # <slug:slug> is a path converter provided by Django
    path("posts/<slug:slug>", views.post_detail, name="post-detail-page")
]
