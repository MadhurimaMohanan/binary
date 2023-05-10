from django.shortcuts import render
from django.views import View


class binary_tree_form(View):
    def get(self,request):
        return render(request,'create_binary.html')

from .models import BinaryTreeNode
from .forms import BinaryTreeNodeForm,SearchForm

def create_node(request):
    if request.method == 'POST':
        form = BinaryTreeNodeForm(request.POST)
        if form.is_valid():
            # Save the new node to the database
            node = form.save()

            # If a parent node was selected, update the parent node's child references
            if form.cleaned_data['parent']:
                parent_node = form.cleaned_data['parent']
                if form.cleaned_data['left_child']:
                    parent_node.left_child = node
                else:
                    parent_node.right_child = node
                parent_node.save()

            return render(request, 'success.html', {'node': node})
    else:
        form = BinaryTreeNodeForm()

    return render(request, 'create_binary.html', {'form': form})

def display_tree(request):
    root_node = BinaryTreeNode.objects.first()
    if root_node:
        return render(request, 'display_tree.html', {'nodes': root_node})
    else:
        return render(request, 'no_tree.html')


def search_node(request):
    
   
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            node = BinaryTreeNode.objects.get(pk=form.cleaned_data['id'])
            parent_id = str(node.parent.id) if node.parent else None
            print(parent_id)
            if form.cleaned_data['direction'] == 'left':
                while node.left_child:
                    node = node.left_child
            else:
                while node.right_child:
                    node = node.right_child

            return render(request, 'display_node.html', {'node': node, 'parent_id': parent_id})
    else:
        form = SearchForm()

    return render(request, 'search.html', {'form': form})


