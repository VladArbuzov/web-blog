from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from .models import Post, Likes, Comments
from .form import CommentsForm, PostForm
from django.http import Http404
from django.contrib.auth.decorators import login_required

class PostView(View):
    '''вывод записей'''
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list': posts})

class PostDetail(View):
    '''записи'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk) # получить по id
        return render(request, 'blog/blog_detail.html',{'post': post})
    
class AddComments(View):
    '''добавление комментариев'''
    def post(self, request, pk):
        try:
            post = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            raise Http404("Post does not exist")

        # Инициализация формы данными пользователя
        form = CommentsForm(request.POST, initial={'name': request.user.username, 'email': request.user.email})

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post-detail', pk=pk)

        return render(request, 'blog/blog_detail.html', {'post': post, 'comments': Comments.objects.filter(post=post), 'form': form})

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, pos_id=pk)
            return redirect(f'/{pk}/')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.pos_id = int(pk)
            new_like.save()
            return redirect(f'/{pk}/')
        
class DelLike(View):
     def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            lik = Likes.objects.get(ip=ip_client)
            lik.delete()
            return redirect(f'/{pk}/')
        except:
            return redirect(f'/{pk}/')
        
def create(request):
    error = ''
    if request.method  == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'
    
    form = PostForm()
    
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'blog/create.html', data)

@login_required
def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post-detail', pk=post.pk)
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/edit_post.html', {'form': form})