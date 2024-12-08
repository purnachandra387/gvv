# forum/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Topic, Post, Comment
from .forms import PostForm, CommentForm

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'forum/category_list.html', {'categories': categories})

def topic_list(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = Topic.objects.filter(category=category)
    return render(request, 'forum/topic_list.html', {'category': category, 'topics': topics})

def post_list(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    posts = Post.objects.filter(topic=topic)
    form = PostForm()
    if request.method == 'POST': 
        form = PostForm(request.POST) 
        if form.is_valid(): 
            post = form.save(commit=False) 
            post.topic = topic
            post.author = request.user 
            post.save()
            return redirect('post_list', topic_id=topic.id) 
    return render(request, 'forum/post_list.html', {'topic': topic, 'posts': posts,'form': form})

def reply_post(request, post_id): 
    parent_post = get_object_or_404(Post, id=post_id) 
    if request.method == 'POST': 
        form = PostForm(request.POST) 
        if form.is_valid(): 
            reply = form.save(commit=False) 
            reply.topic = parent_post.topic 
            reply.parent = parent_post 
            reply.author = request.user 
            reply.save() 
            return redirect('post_list', topic_id=parent_post.topic.id) 
    else: 
        form = PostForm() 
        return render(request, 'forum/reply_post.html', {'parent_post': parent_post, 'form':form})
    
def post_detail(request,pk):
    post = get_object_or_404(Post, pk=pk) 
    comments = post.comments.all() 
    if request.method == 'POST': 
        form = CommentForm(request.POST) 
        if form.is_valid(): 
            comment = form.save(commit=False) 
            comment.post = post 
            comment.author = request.user 
            comment.save() 
            return redirect('post_detail', pk=post.pk) 
    else: 
        form = CommentForm() 
    return render(request, 'forum/post_detail.html', {'post': post, 'comments': comments, 'form': form})