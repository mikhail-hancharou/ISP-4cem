from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Blog, Category


def blog(request):
    return render(request, "blog/blog.html")


class BlogListView(ListView):
    paginate_by = 2
    model = Blog
    template_name = 'base.html'

    # queryset = Blog.objects.order_by('-publication_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_categories'] = Category.objects.all()
        return context
