from blog.models import Blog, Category
from asgiref.sync import sync_to_async


@sync_to_async
def get_posts_by_category(category):
    return Blog.objects.filter(categories__title=category)


@sync_to_async
def get_authors_blog(user_blog_pk):
    return Blog.objects.filter(author__pk=user_blog_pk)


@sync_to_async()
def get_all_categories():
    return Category.objects.all()


@sync_to_async()
def get_ordered_posts(criteria):
    return Blog.objects.order_by(criteria)
