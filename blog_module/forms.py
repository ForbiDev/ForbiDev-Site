from django.forms import ModelForm

from .models import PostComment


class CommentForm(ModelForm):
    class Meta:
        model = PostComment
        fields =