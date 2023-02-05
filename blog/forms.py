
from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','desc']
        labels = {'title' : '', 'desc' : ''}
        widgets = {'title' : forms.TextInput(attrs={'class' : 'form-control','style':'width:20%;margin:10px;padding:10px;font-size:larger;','placeholder':'Title'}),'desc':forms.Textarea(attrs={'class':'form-control','style':'width:80%;margin:10px;display:block;font-size:larger;padding:10px','rows':'15','placeholder':'write your blog here...'}), }
