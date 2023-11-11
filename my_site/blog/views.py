from django.shortcuts import render, get_object_or_404

from .models import Post

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
    return render(request, "blog/post-details.html", {
        "post": identified_post,
        "tags": post_tags
    })
