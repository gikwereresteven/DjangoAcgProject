from django import forms
from .models import Post

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput( 
    attrs={'size':'32', 'class':'inputText'}))
    email = forms.EmailField(max_length=100, widget=forms.TextInput( 
    attrs={'size':'32', 'class':'inputText'}))
    message = forms.CharField(widget=forms.Textarea(attrs={"rows":5, "cols":31}))

    class Meta:
        model = Post
        fields = ('name','email','message',)