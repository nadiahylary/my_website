from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, DetailView

from blog.models import Post


# from .blog_posts_dict import blog_posts

"""def get_date(post):
    return post.date_created
"""
# Create your views here.


class IndexListView(ListView):
    template_name = "blog/index.html"
    model = Post
    context_object_name = "posts"
    ordering = ['-date_created']

    def get_queryset(self):
        queryset = super().get_queryset()
        data = queryset[:3]
        return data


# def index(request):
#     blog_posts = Post.objects.all().order_by("-date_created")[:3]
#     # sorted_posts = sorted(blog_posts, key=get_date)
#     # latest_posts = blog_posts
#     return render(request, "blog/index.html", {
#         "posts": blog_posts,
#
#     })


"""response_data = ""
    for key in blog_posts.keys():
        print(key)
        post_path = reverse("detail-post-page", args=[key])
        response_data += f"<div><p><a href = '{post_path}'>" + key + "</a></p></div"
    return HttpResponse(f"<h1>Welcome to my blog!</h1><h2>Some recent blog posts</h2>{response_data}")"""


class AllPostsView(ListView):
    template_name = "blog/all-posts.html"
    model = Post
    context_object_name = "posts"
    ordering = ['-date_created']


# def posts(request):
#     blog_posts = Post.objects.all().order_by("-date_created")
#     # sorted_posts = sorted(blog_posts, key=get_date)
#     return render(request, "blog/all-posts.html", {
#         "posts": blog_posts,
#
#     })


"""response_data = ""
    for key in blog_posts.keys():
        # post_path = reverse("single-post", args=[key])
        print(key)
        response_data += f"<li><a href = '{detail_post(request, key)}'>" + key + "</a></li>"
    response_data = f"<h1>All blog posts</h1><ul>{response_data}</ul>"
    return HttpResponse(response_data)"""


class DetailPostView(DetailView):
    template_name = "blog/detail-post.html"
    model = Post
    context_object_name = "post"


def detail_post(request, slug):
    """post_detail = None
    for post in blog_posts:
        if post['slug'] == slug:
            post_detail = post"""
    blog_post = get_object_or_404(Post, slug=slug)
    # post_detail = next(post for post in blog_post)
    return render(request, "blog/detail-post.html", {
        'post': blog_post
    })


"""try:
        response_data = "<h1>" + post_title + "</h1>"
        response_data += "<p>" + blog_posts[post_title] + "</p>"
        return HttpResponse(response_data)
    except:
        raise Http404()"""


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")
