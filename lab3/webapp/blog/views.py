import logging

from django.contrib import messages
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from blog.forms import AddBlogForm
from blog.models import Blog, Category

logger = logging.getLogger('django')


def blog(request):
    return render(request, "home.html")


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
    model = Blog
    template_name = 'home.html'

    # queryset = Blog.objects.order_by('-publication_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        print(context)
        return context


class CategoryPostList(ListView):
    paginate_by = 2
    template_name = 'posts_by_category.html'

    def get_queryset(self):
        return Blog.objects.filter(categories__title=self.kwargs['category'])


class BlogDetailView(DetailView):
    model = Blog
    template_name = 'post_detail.html'


class BlogUpdateView(UpdateView):
    form_class = AddBlogForm
    template_name = 'blog/post_edit.html'
    success_url = reverse_lazy('post_detail')

    def get_object(self, queryset=None):
        obj = super(BlogUpdateView, self).get_object(queryset)
        if obj.author != self.request.user:
            messages.error(self.request, "You can't edit this post")
            logger.error("Attempt to get an access to update function")
            raise Http404("You don't own this object")
        return obj


'''class BlogUpdateView(UpdateView):
    model = Blog
    template_name = 'post_edit.html'
    fields = ['title', 'content', 'categories']

    def get_object(self, queryset=None):
        obj = super(BlogUpdateView, self).get_object(queryset)
        if obj.author != self.request.user:
            messages.error(self.request, "You can't edit this post")
            logger.error("Attempt to get an access to update function")
            raise Http404("You don't own this object")
        return obj'''


class BlogDeleteView(DeleteView):
    model = Blog
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        obj = super(BlogDeleteView, self).get_object(queryset)
        if obj.author != self.request.user:
            messages.error(self.request, "You can't edit this post")
            logger.error("Attempt to get an access to delete function")
            raise Http404("You don't own this object")
        return obj
