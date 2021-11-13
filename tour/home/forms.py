from django import forms
from home.models import Customer_Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Customer_Comment
        fields = "__all__"