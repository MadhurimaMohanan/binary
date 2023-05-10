from django.db import models
from mptt.models import MPTTModel

# Create your models here.
class BinaryTreeNode(MPTTModel):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    left_child = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='leftchild')
    right_child = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='rightchild')

    def __str__(self):
        return self.name
