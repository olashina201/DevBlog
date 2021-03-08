from django.shortcuts import render, get_object_or_404
from . models import Post, Category
from django.views.generic import CreateView, DetailView, ListView

# Create your views here.


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 5

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(PostListView, self).get_context_data(*args, **kwargs) 
        context["cat_menu"] = cat_menu
        return context


def CategoryView(request, cats):
    category_post = Post.objects.filter( genre__name = cats )
    return render(request, 'blog/category.html', {'cats':cats, 'category_post':category_post})



def about(request):
    return render(request, 'blog/about.html', {'title': 'About-Us'})


def list(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/blog-list.html', context)


class BlogPostListView(ListView):
    model = Post
    template_name = "blog/blog-list.html"
    context_object_name = 'posts'
    ordering = ['-date']
    paginate_by = 10



class PostDetailView(DetailView):
    model = Post
    template_name = "blog/blog-post.html"

