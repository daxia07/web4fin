from django.urls import path
from . import views

urlpatterns = [
    path('post-comment/<int:post_id>', views.post_comment, name='post_comment'),
    path('post-comment/<int:post_id>/<int:parent_comment_id>', views.post_comment, name='comment_reply')
]
