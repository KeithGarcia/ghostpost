from django import forms
from homepage.models import boastroast

class AddPostForm(forms.ModelForm):
    class Meta:
        model = boastroast
        fields = ["choices", "post_field"]