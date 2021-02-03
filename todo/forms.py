from django import forms
from .models import Column, Todo


'''
    This is the form for Column model
    All attributes are mentioned and required
'''
class ColumnForm(forms.ModelForm):
    title = forms.CharField(max_length=20)
    icon = forms.CharField(max_length=20, required=False)
    palette = forms.CharField(max_length=20, required=False)

    class Meta:
        model = Column
        fields = ('title', 'icon', 'palette')


'''
    This is the form for Todo model
    The column attribute is not mandatory because it will be handled and set in the view
    But other attributes are handled by this form
'''
class TodoForm(forms.ModelForm):
    title = forms.CharField(max_length=20)
    description = forms.CharField(max_length=500)
    column = forms.ModelChoiceField(queryset=Column.objects.all())
    palette = forms.CharField(max_length=20, required=False)
    link = forms.CharField(max_length=100, required=False)
    attachment = forms.FileField(required=False)

    class Meta:
        model = Todo
        fields = ('title', 'description', 'palette', 'link', 'attachment')