from django.forms import ModelForm, Textarea
from blogapp.models import *

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'slug',]
        widgets = {'body': Textarea(attrs={'cols': 80, 'rows': 15}), }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        exclude = ["post"]
        widgets = {'body': Textarea(attrs={'placeholder': 'Enter your comment...'}), }



