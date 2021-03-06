from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from blog.models import Post
from comments.forms import CommentForm
from .models import Comment


@login_required(login_url='/login/')
def post_comment(request, post_id, parent_comment_id=None):
    article = get_object_or_404(Post, id=post_id)
    initial_data = {
        "content_type": article.get_content_type,
        "object_id": article.id
    }
    comment_form = CommentForm(request.POST or None, initial=initial_data)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            content_type = ContentType.objects.get_for_model(article.__class__)
            new_comment.content_type = content_type
            new_comment.object_id = post_id
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
        comments = Comment.objects.filter_by_instance(article)
        context = {
            'comments': comments,
            'comment_form': comment_form
        }
        return render(request, 'comments/reply.html', context)
