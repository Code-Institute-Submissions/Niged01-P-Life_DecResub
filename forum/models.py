from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from django_resized import ResizedImageField
from tinymce.models import HTMLField
from hitcount.models import HitCountMixin, HitCount
from django.contrib.contenttypes.fields import GenericRelation
from taggit.managers import TaggableManager


STATUS = ((0, "Draft"), (1, "Published"))



class Author(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=40, blank=True)
    slug = slug = models.SlugField(max_length=400, unique=True, blank=True)
    bio = HTMLField()
    points = models.IntegerField(default=0)
    profile_pic = ResizedImageField(size=[50, 80], quality=100, upload_to="authors", default=None, null=True, blank=True)

    def __str__(self):
        return self.fullname

    @property
    def num_posts(self):
        return Post.objects.filter(user=self).count()
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)
        super(Author, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    description = models.TextField(default="description")

    class Meta:
        verbose_name_plural = "categories"
    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Category, self).save(*args, **kwargs)

    def get_url(self):
        return reverse("posts", kwargs={
            "slug":self.slug
        })

    @property
    def num_posts(self):
        return Post.objects.filter(categories=self).count()
    
    @property
    def last_post(self):
        return Post.objects.filter(categories=self).latest("date")


class Reply(models.Model):
    user = models.ForeignKey(Author, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:100]

    class Meta:
        verbose_name_plural = "replies"


class Post(models.Model):
    title = models.CharField(max_length=400, unique=True, blank=True)
    post_image = ResizedImageField(size=[50, 80], quality=100, upload_to="posts", default=None, null=True, blank=True)
    slug = models.SlugField(max_length=400, unique=True, blank=True)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = HTMLField()
    categories = models.ManyToManyField(Category)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    hit_count_generic = GenericRelation(
        HitCount, object_id_field='object_pk',
        related_query_name='hit_count_generic_relation'
    )
    tags = TaggableManager()
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
    
    


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"