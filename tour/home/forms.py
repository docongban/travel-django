from django import forms
from home.models import Customer_Comment, booktour

class CommentForm(forms.ModelForm):
    class Meta:
        model = Customer_Comment
        fields = "__all__"

class BookForm(forms.ModelForm):
    class Meta:
        model = booktour
        fields = "__all__"
