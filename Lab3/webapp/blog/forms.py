from django import forms
from .models import *


class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'content', 'photo', 'categories']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 70, 'rows': 15})
        }

    categories = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Category.objects.all(),
        required=True)


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {'content': forms.Textarea(attrs={'cols': 60, 'rows': 5})}

    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 5}), required=True)

