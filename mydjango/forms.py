from django import forms 
from .models import Bookmark
class BookmarkForm(forms.ModelForm):
    class Meta:
        model = Bookmark
        fields = {'title', 'url', 'memo'}
        # fields = '_all_'
