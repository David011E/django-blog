from .models import Comments
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)