# importing models and libraries
from django.views import generic

from .models import Posts


# class based views for posts
class PostsList(generic.ListView):
    queryset = Posts.objects.filter(status=1).order_by('-created_on')
    template_name = 'home.html'
    paginate_by = 4


# class based view for each post
class PostDetail(generic.DetailView):
    model = Posts
    template_name = "post.html"
