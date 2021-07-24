from django.shortcuts import render
from django.db import transaction
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.views.generic import ListView, DetailView
from .models import Post, Category, Tag, Comment
from django.db.models import F
from django.template.defaulttags import register
from .utils import create_comments_tree
from .forms import CommentForm


@register.filter
def get_all_tag(value):
    return Tag.objects.all()

@register.filter
def get_all_category(value):
    return Category.objects.all()

def get_rubrics_tag(self, context):
    if self.request.LANGUAGE_CODE == "ru":
        context['title_rubrics'] = 'Все рубрики'
    if self.request.LANGUAGE_CODE == "en":
        context['title_rubrics'] = 'All rubrics'

    if self.request.LANGUAGE_CODE == "ru":
        context['title_tag'] = 'Все теги'
    if self.request.LANGUAGE_CODE == "en":
        context['title_tag'] = 'All tag'


class Home(ListView) :
    model = Post
    template_name = 'news/news.html'
    context_object_name = 'posts'
    paginate_by = 2

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        get_rubrics_tag(self, context)

        return context


class PostsByCategory(ListView):
    template_name = 'news/news.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.LANGUAGE_CODE == "ru":
            buffer = Category.objects.get(slug=self.kwargs['slug'])
            context['title'] ="Категория " + buffer.name_ru
        if self.request.LANGUAGE_CODE == "en":
            buffer = Category.objects.get(slug=self.kwargs['slug'])
            context['title'] = "Category "+buffer.name_en

        return context



class PostsByTag(ListView):
    template_name = 'news/news.html'
    context_object_name = 'posts'
    paginate_by = 4
    allow_empty = False

    def get_queryset(self):
        return Post.objects.filter(tags__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        buffer = Tag.objects.get(slug=self.kwargs['slug'])
        get_rubrics_tag(self, context)
        if self.request.LANGUAGE_CODE == "ru":
            context['title'] = 'Записи по тегу ' + str(buffer.name_ru)
        if self.request.LANGUAGE_CODE == "en":
            context['title'] = 'Entries by tag ' + str(buffer.name_en)

        return context


class GetPost(DetailView):
    model = Post
    template_name = 'news/newsdetails.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        get_rubrics_tag(self, context)
        self.object.views = F('views') + 1
        self.object.save()
        # self.object.refresh_from_db()
        return context

def base_view(request):
    comments = Post.objects.first().comment.all()
    result = create_comments_tree(comments)
    comment_form = CommentForm(request.POST or None)
    return render(request, 'news/comments.html', {'comments': result, 'comment_form': comment_form})

def create_comment(request):
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.user = request.user
        new_comment.text = comment_form.cleaned_data['text']
        new_comment.content_type = ContentType.objects.get(model='post')
        new_comment.object_id = 1
        new_comment.parent = None
        new_comment.is_child = False
        new_comment.save()
    return HttpResponseRedirect('/post-comments')


@transaction.atomic
def create_child_comment(request):
    user_name = request.POST.get('user')
    current_id = request.POST.get('id')
    text = request.POST.get('text')
    user =User.objects.get(username=user_name)
    content_type = ContentType.objects.get(model='post')
    parent = Comment.objects.get(id=int(current_id))
    is_child = False if not parent else True
    Comment.objects.create(
        user=user, text=text, content_type=content_type, object_id=1,
        parent=parent, is_child=is_child
    )
    comments_ = Post.objects.first().comments.all()
    comments_list = create_comments_tree(comments_)
    return render(request, 'news/comments.html', {'comments': comments_list})