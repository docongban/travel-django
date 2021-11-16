from django import forms
from home.models import Customer_Comment, booktour

class CommentForm(forms.ModelForm):
    class Meta:
        model = Customer_Comment
        fields = "__all__"

class BookForm(forms.ModelForm):
    class Meta:
        model = booktour
        fields = ('cus_id','cus_name','cus_add','cus_mail','cus_phone','cus_soluong',)
