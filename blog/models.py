from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption


class Post(models.Model):
    title = models.CharField(max_length=150)
    slug = models.SlugField(default="", blank=True,
                            null=False, db_index=True, unique=True)
    image = models.ImageField(upload_to="images")
    date_created = models.DateTimeField()
    excerpt = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(500)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL,
                               null=True, related_name="posts")
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def absolute_url_slug(self):
        return reverse("detail-post-page", args=[self.slug])

    def save(self, *args, **kwargs):
        # self.image = "blog/images/"+self.image
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)
