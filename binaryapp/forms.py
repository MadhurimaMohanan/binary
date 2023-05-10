from django import forms


from django import forms
from .models import BinaryTreeNode

class BinaryTreeNodeForm(forms.ModelForm):
    name = forms.CharField(max_length=100)
    id = forms.IntegerField()
    parent = forms.ModelChoiceField(
        queryset=BinaryTreeNode.objects.all(),
        empty_label="Select Parent Node",
        required=False
    )
    left_child = forms.ModelChoiceField(
        queryset=BinaryTreeNode.objects.all(),
        required=False,
        empty_label="No Left Child"
    )
    right_child = forms.ModelChoiceField(
        queryset=BinaryTreeNode.objects.all(),
        required=False,
        empty_label="No Right Child"
    )

    class Meta:
        model = BinaryTreeNode
        fields = ('name', 'id', 'parent', 'left_child', 'right_child')


class SearchForm(forms.Form):
    id = forms.IntegerField(label='ID')
    direction = forms.ChoiceField(choices=[('left', 'Left'), ('right', 'Right')], widget=forms.RadioSelect)
