from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post
from comments.forms import CommentForm
from .models import Comment


@login_required(login_url='/login/')
def post_comment(request, article_id, parent_comment_id=None):
    article = get_object_or_404(Post, id=article_id)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.content_type = Post
            new_comment.object_id = article_id
            new_comment.author = request.user

            if parent_comment_id:
                parent_comment = Comment.objects.get(id=parent_comment_id)
                new_comment.parent_id = parent_comment.get_root().id
                new_comment.reply_to = parent_comment.user
                new_comment.save()
                return HttpResponse('200 OK')

            new_comment.save()
            return redirect(article)
        else:
            return HttpResponse("The form is incorrect, please fill in again")
    elif request.method == 'GET':
        comments = Comment.objects.filter(object_id=article_id, content_object=Post)
        context = {
            'comments': comments
        }
        return render(request, 'comments/reply.html', context)
