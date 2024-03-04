from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import View
from django.views.generic.edit import CreateView

from .models import Post, Comment

# Create your views here.


def starting_page(request):
    posts = Post.objects.all().order_by("-date")[:3]
    return render(request, "blog/index.html", {
        "posts": posts
    })


def posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": posts
    })


def post_detail(request, slug):
    identified_post = get_object_or_404(Post, slug=slug)
    post_tags = identified_post.tags.all()
    is_read_later = request.session.get("read-later") == identified_post.id
    comments = Comment.objects.filter(post_id=identified_post)
    return render(request, "blog/post-details.html", {
        "post": identified_post,
        "tags": post_tags,
        "is_read_later": is_read_later,
        "comments": comments
    })


class ReadLaterView(View):
    def get(self, request):
        read_later_post_id = request.session.get("read-later")
        post = Post.objects.filter(pk=read_later_post_id)
        return render(request, "blog/post-read-later.html", {
            "all_posts": post
        })

    def post(self, request):
        post_id = request.POST["post_id"]
        post_slug = request.POST["post_slug"]
        request.session["read-later"] = int(post_id)
        return HttpResponseRedirect(reverse("post-detail-page", args=[post_slug]))


class AddCommentView(View):
    def post(self, request):
        post_id = Post.objects.get(pk=request.POST["post_id"])
        user_name = request.POST["name"]
        comment = request.POST["comment"]
        post_slug = request.POST["post_slug"]

        new_comment = Comment(post_id=post_id, name=user_name, text=comment)
        new_comment.save()

        return HttpResponseRedirect(reverse("post-detail-page", args=[post_slug]))
