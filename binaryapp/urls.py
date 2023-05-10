from django.urls import path
from django.urls import re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from binaryapp import views

from .views import create_node,binary_tree_form,display_tree,search_node

urlpatterns=[
    path('create_node/',create_node),
    path('display_tree/',display_tree),
    path('search_node/',search_node),
    path('binary_tree_form/',binary_tree_form.as_view()),
]