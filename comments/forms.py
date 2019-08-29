from django import forms
from comments.models import Comment
# from ckeditor.widgets import CKEditorWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        widgets = {
            'content_type': forms.HiddenInput(),
            'object_id': forms.HiddenInput(),
            'parent_id': forms.HiddenInput(),
        }
        fields = ['content']

    def get_comment_model(self):
        return Comment


#
# class CommentForm(forms.Form):
#     content_type = forms.CharField(widget=forms.HiddenInput)
#     object_id = forms.IntegerField(widget=forms.HiddenInput)
#     parent_id = forms.CharField(widget=forms.HiddenInput, required=False)
#     content = forms.CharField(widget=CKEditorWidget(config_name='comments'))
#
#     def get_comment_model(self):
#         return Comment
#
#     def is_valid(self):
#         self.data['parent'] = self.cleaned_data['parent']
#         return super().is_valid()





