from django import forms

from .models import PostComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = ['fullname', 'email', 'content']
        widgets = {
            'full_name': forms.TextInput(),
            'email': forms.EmailInput(),
            'content': forms.Textarea(),
        }