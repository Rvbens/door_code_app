from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, UpdateView
from .models import Post
from .signals import home_signal
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    context = { 'posts': Post.objects.all()}
    ip = request.META.get('REMOTE_ADDR')
    home_signal.send(sender=None, usuario=request.user.username, ip=ip)#send signal to log user activity
    return render(request,"blog/home.html",context)


class HomeView(LoginRequiredMixin, ListView):#unused
    model = Post
    template_name = "blog/home.html"
    context_object_name = "posts"
    ordering = ["-date_posted"]
    paginate_by = 5

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title","content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False