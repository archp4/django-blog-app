# Generated by Django 4.2.4 on 2023-09-03 11:39

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('postId', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('description', tinymce.models.HTMLField()),
                ('content', models.TextField()),
                ('imageUrl', models.CharField(max_length=256)),
                ('addDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('catId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category')),
            ],
        ),
    ]
