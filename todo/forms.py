from django import forms
from .models import Todo
 
 
class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = "__all__"
        widgets = {
            'details': forms.Textarea(attrs={'cols': 30, 'rows': 10}),
        }
