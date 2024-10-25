from django.db import models
from django import forms
from .models import Post
from django.shortcuts import render, redirect
from .forms import PostForm, PostModelForm


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    rate = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class PostForm(forms.Form):
    title = forms.CharField(max_length=200, required=True)
    content = forms.CharField(widget=forms.Textarea, required=True)

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        def create_post(request):
            if request.method == 'POST':
                form = PostModelForm(request.POST)  # Используйте PostForm для обычной формы
                if form.is_valid():
                    form.save()
                    return redirect('post_list')  # Здесь укажите имя вашего URL для списка постов
            else:
                form = PostModelForm()  # Или PostForm()

            return render(request, 'create_post.html', {'form': form})

