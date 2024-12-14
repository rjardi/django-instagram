from django.forms import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from posts.models import Post
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .forms import PostCreateForm
from django.contrib import messages
# Create your views here.

@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    
    template_name="posts/post_create.html"
    model=Post
    form_class=PostCreateForm
    success_url=reverse_lazy("home")

    def form_valid(self, form):
        form.instance.user=self.request.user
        messages.add_message(self.request, messages.SUCCESS, "Publicación creada correctamente")
        return super(PostCreateView, self).form_valid(form)
    

@method_decorator(login_required, name="dispatch")
class PostDetailView(DetailView):
    
    template_name="posts/post_detail.html"
    model=Post
    context_object_name="post"

@login_required
def like_post(request, pk):

    post=Post.objects.get(pk=pk)
    if request.user in post.likes.all():
        messages.add_message(request, messages.INFO, "Ya no te gusta esta publicación")
        post.likes.remove(request.user)
    else:   
        post.likes.add(request.user)
        messages.add_message(request, messages.INFO, "Te gusta esta publicación")

    return HttpResponseRedirect(reverse('post_detail', args=[pk]))

@login_required
def like_post_ajax(request, pk):

    post=Post.objects.get(pk=pk)
    if request.user in post.likes.all():
        post.likes.remove(request.user)
        return JsonResponse(
            {
            'message':'Ya no te gusta esta publicación',
            'liked':False
            }
        )
    else:   
        post.likes.add(request.user)
        return JsonResponse(
            {
            'message':'Te gusta esta publicación',
            'liked':True
            }
        )






    