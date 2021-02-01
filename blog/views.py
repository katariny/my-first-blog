from urllib import request

import form as form
from django.shortcuts import render
from .forms import PostForm, ComentForm
from django.utils import timezone
from blog.models import Post, Comentario
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect


#def home(request): #parametro
 #   now = datetime.datetime.now()
  #  html = "<html><body>Agora são %s,</body></html>" %now
   # return HttpResponse(html)
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # posts = Post.objects.filter(title__startswith='s')
    #context = {
     #   'posts': posts,
      #  'titulo': 'lalalalad',
       # 'teste1': {
        #    'nome': 'jefferson',
         #   'idade': 123,
       # }
   # }
    #return render(request, 'blog/post_list.html', context)

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # posts = Post.objects.filter(title__startswith='s')
    context = {
        'posts': posts,
        'titulo': 'lalalalad',
        'teste1': {
            'nome': 'jefferson',
            'idade': 123,
        }
    }
    return render(request, 'blog/post_list.html', context)



def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = Comentario.objects.filter(post=post)
    context = {
        'post': post,
        'comentarios': comentarios
    }
    return render(request, "blog/post_detail.html", context)


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})


def post_coment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = ComentForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.post = post
            #post.published_date = timezone.now()
            comentario.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = ComentForm()
    return render(request, 'blog/coment_edit.html', {'form': form})


# def coment_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, "blog/coment_list.html", {'form': form})






#teste
#def home(request):
 #   now = database.datatime.now()
  #  return render(request, 'blog/home.html')