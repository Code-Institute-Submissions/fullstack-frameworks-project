from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from .models import Post, Comment
from .forms import BlogPostForm, CommentForm
from django.core.paginator import Paginator

ITEMS_PER_PAGE = 3


def get_posts(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'blogposts.html' template
    Pagination included
    """
    posts = Post.objects.all().order_by('-published_date')

    paginator = Paginator(posts, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    posts = paginator.page(page)
    return render(request, "blogposts.html", {'posts': posts})


def get_posts_by_tag(request, tag):
    posts = Post.objects.filter(tag=tag).order_by('-published_date')

    paginator = Paginator(posts, ITEMS_PER_PAGE)

    page = request.GET.get('page')

    # If there is no page parameter in URL, set page to 1

    if(page is None):
        page = 1

    posts = paginator.page(page)
    return render(request, "blogposts.html", {'posts': posts})


def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('login')

        else:
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                comment.post = post
                comment.save()
                messages.success(request, "Thanks for your comment, it has been sent for approval!")

                return redirect(post_detail, post.pk)

    else:
        form = CommentForm()
        return render(request, "postdetail.html", {'post': post, 'form': form})


def create_or_edit_post(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    post = get_object_or_404(Post, pk=pk) if pk else None
    if request.method == "POST":
        form = BlogPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect(post_detail, post.pk)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'blogpostform.html', {'form': form})


def delete_comment(request, pk, rk):
    if request.user.is_authenticated:
        user = request.user 
        comment = get_object_or_404(Comment, pk=rk)
        comment.delete()
        messages.success(request, "Your comment is deleted.")
    
    return redirect(post_detail, pk)
   