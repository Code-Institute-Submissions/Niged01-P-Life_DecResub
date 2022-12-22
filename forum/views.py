from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Author, Category, Post
from .utils import update_views
from .forms import CommentForm, PostForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def index(request):
    """ home page view """

    return render(request, 'index.html')


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6


def profile(request):
    """ profile page view """
    return render(request, 'profile.html')


def my_posts(request):
    """ authenticated user can view their own blogs """

    author = get_object_or_404(Author, user=request.user)
    logged_in_user_posts = list(Post.objects.filter(author=author))
    return render(request, 'my_posts.html', {'posts': logged_in_user_posts})


def edit_post(request, post_id):
    """ users that are authenticated can edit their own post """
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=post)
        if post_form.is_valid():
            form = post_form.save(commit=False)
            form.approved = False
            messages.success(
                request,
                'Updated post has been successfully submitted for approval'
            )
            form.save()
            return redirect('my_posts')
    post_form = PostForm(instance=post)
    context = {'post_form': post_form}
    return render(request, 'edit_posts.html', context)


def delete_post(request, post_id):
    """ Authenticated users can delete their own posts"""
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    messages.success(request, 'Post deleted!')
    return redirect('my_posts')


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        update_views(request, post)

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def create_post(request):
    context = {}
    form = PostForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            print("\n\n its valid")
            author = Author.objects.get(user=request.user)
            new_post = form.save(commit=False)
            new_post.author = author
            new_post.save()
            form.save_m2m()
            messages.success(
                request,
                'Updated post has been successfully submitted for approval'
            )
            return HttpResponseRedirect(reverse('home'))
    context.update({
        "form": form,
        "title": "PLife: Create New Post"
    })
    return render(request, "create_post.html", context)
