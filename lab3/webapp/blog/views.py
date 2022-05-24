import logging

from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from blog.forms import AddBlogForm
from blog.models import Blog, Category

logger = logging.getLogger('django')


class BlogCreateView(CreateView):
    form_class = AddBlogForm
    template_name = 'blog/post_new.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super(BlogCreateView, self).form_valid(form)


class BlogListView(ListView):
    paginate_by = 4
    # model = Blog
    template_name = 'home.html'

    queryset = Blog.objects.order_by('-time_create')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        print(context)
        return context


class CategoryPostList(ListView):
    paginate_by = 4
    template_name = 'blog/posts_by_category.html'
    context_object_name = 'blogs_with_category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.kwargs['category']
        print(context)
        return context

    def get_queryset(self):
        return Blog.objects.filter(categories__title=self.kwargs['category'])


class MyPostsList(ListView):
    template_name = 'blog/my_posts.html'
    context_object_name = 'my_blogs'

    def get_queryset(self):
        return Blog.objects.filter(author__pk=self.request.user.pk)


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/post_detail.html'

    form_class = AddBlogForm
    template_name = 'blog/post_new.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return super(BlogDetailView, self).form_valid(form)


class BlogUpdateView(UpdateView):
    model = Blog
    form_class = AddBlogForm
    template_name = 'blog/post_edit.html'


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        obj = super(BlogDeleteView, self).get_object(queryset)
        if obj.author != self.request.user:
            messages.error(self.request, "You can't edit this post")
            logger.error(f"Attempt to get an access to delete function{obj.author} - {self.request.user}")
            raise Http404("You don't own this object")
        return obj
