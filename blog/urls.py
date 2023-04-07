from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexListView.as_view(), name="index-page"),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name="detail-post-page"),
    path("posts", views.AllPostsView.as_view(), name="posts-page"),
    path("read-later", views.ReadLaterView.as_view(), name="read-later"),
    # path("", views.index, name="index-page"),
    # path("posts", views.posts, name="posts-page"),
    # path("posts/<slug:slug>", views.DetailPostView.as_view(), name="detail-post-page"),
    # path("posts/<slug:slug>", views.detail_post, name="detail-post-page"),
    path("about",  views.about, name="about-page"),
    path("contact",  views.contact, name="contact-page")

]
