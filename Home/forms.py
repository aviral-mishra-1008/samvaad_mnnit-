# forms.py
from django import forms
from .models import Submissions

class ArticleSubForm(forms.ModelForm):
    class Meta:
        model = Submissions
        fields = ['unique_id','name', 'email_id', 'heading', 'estimated_time', 'article', 'image', 'insta', 'reg_no', 'branch','year', 'phone_no']
