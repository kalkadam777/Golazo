from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    title = forms.CharField(required=True,
                            max_length=100,
                            widget=forms.widgets.Textarea(
                                attrs={"placeholder": "Enter The Title:",
                                       "class": "form-control"}),
                            label="")
    content = forms.CharField(required=True,
                              max_length=500,
                              widget=forms.widgets.Textarea(
                                  attrs={"placeholder": "Fill The Content:",
                                         "class": "form-control"}),
                              label="")

    class Meta:
        model = Article
        exclude = ("author", "created_at")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', 'author']

    content = forms.CharField(
        widget=forms.Textarea(attrs={"placeholder": "Add a comment...", "class": "form-control"}),
        label="",
        required=True
    )