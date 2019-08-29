from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.db.models import Q
from mptt.models import MPTTModel, TreeForeignKey, TreeManager


class CommentManager(TreeManager):
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        object_id = instance.id
        var_filter = Q(object_id=object_id) & Q(content_type=content_type)
        return super(CommentManager, self).filter(var_filter)


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

    objects = CommentManager()

    class MPTTMeta:
        order_insertion_by = ['created']

    def __unicode__(self):
        return str(self.author.username)

    def __str__(self):
        return str(self.author.username)
