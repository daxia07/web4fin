from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

# from blog.models import Post


class Comment(MPTTModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(blank=False)
    created = models.DateTimeField(auto_now_add=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    reply_to = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='replyers')

    class MPTTMeta:
        order_insertion_by = ['created']

    def __unicode__(self):
        return str(self.author.username)

    def __str__(self):
        return str(self.author.username)
