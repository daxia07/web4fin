from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    def is_valid(self):
        return super().is_valid()

    class Meta:
        model = Comment
        fields = ['content']
