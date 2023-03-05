from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index-page"),
    path("posts", views.posts, name="posts-page"),
    path("posts/<slug:slug>", views.detail_post, name="detail-post-page"),
    path("about",  views.about, name="about-page"),
    path("contact",  views.contact, name="contact-page")
]
