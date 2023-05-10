# Generated by Django 4.2 on 2023-05-10 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('binaryapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BinaryTreeNode',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('left_child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='leftchild', to='binaryapp.binarytreenode')),
                ('parent_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='binaryapp.binarytreenode')),
                ('right_child', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rightchild', to='binaryapp.binarytreenode')),
            ],
        ),
        migrations.DeleteModel(
            name='BinaryTreeAccount',
        ),
    ]
