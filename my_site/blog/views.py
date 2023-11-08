from datetime import date

from django.shortcuts import render

from .models import Post

# all_posts = [
#     {
#         "slug": "hike-in-the-mountains",
#         "image": "mountains.jpg",
#         "author": "Diego",
#         "date": date(2021, 7, 21),
#         "title": "Mountain Hiking",
#         "excerpt": "There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
#         "content": """
#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "programming-is-fun",
#         "image": "coding.jpg",
#         "author": "Diego",
#         "date": date(2022, 3, 10),
#         "title": "Programming Is Great!",
#         "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
#         "content": """
#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     },
#     {
#         "slug": "into-the-woods",
#         "image": "woods.jpg",
#         "author": "Diego",
#         "date": date(2020, 8, 5),
#         "title": "Nature At Its Best",
#         "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
#         "content": """
#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.

#             Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
#             aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
#             velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
#         """
#     }
# ]


def get_date(post):
    return post['date']

# Create your views here.


def starting_page(request):
    posts = Post.objects.all().order_by("-date")
    # sorted_posts = sorted(all_posts, key=get_date)
    # latest_posts = sorted_posts[-3:] # Get the last 3 items in the list
    return render(request, "blog/index.html", {
        "posts": posts
    })


def posts(request):
    posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts": posts
    })


def post_detail(request, slug):
    # get the post with the given slug
    # identified_post = next(post for post in all_posts if post['slug'] == slug)
    identified_post = Post.objects.get(slug=slug)
    return render(request, "blog/post-details.html", {
        "post": identified_post
    })
