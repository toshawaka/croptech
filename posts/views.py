from django.http import HttpResponse
from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.db.models import Q, Count

from .models import Tag, Technote, Dictionary, Researchers

# Create your views here.

class TechnoteListView(ListView):
    model = Technote
    paginate_by = 5

    def get_queryset(self):
        queryset = Technote.objects.order_by('-created_at').prefetch_related('tag')
        keyword = self.request.GET.get('quick')
        if keyword:
            queryset = queryset.filter(
                Q(key_words__icontains=keyword)
            )
        return queryset

class TechnoteDetailView(DetailView):
    model = Technote

class TagListView(ListView):
    model = Tag
    queryset = Tag.objects.annotate(
        num_posts=Count('technote')).order_by('-num_posts')

class TagView(TechnoteListView):

    def get_queryset(self):
        """タグで絞り込み"""
        tag_name = self.kwargs['tag']
        self.tag = Tag.objects.get(name=tag_name)
        queryset = super().get_queryset().filter(tag=self.tag).order_by('-created_at')
        return queryset

    def get_context_data(self, *args, **kwargs):
        """クリックされたタグを保持"""
        context = super().get_context_data(*args, **kwargs)
        context['tag'] = self.tag
        return context

def top(request):
    return render(request, 'posts/top.html')

def technote(request):
    latest_articles = Article.objects.order_by('-created_at')[:5]
    return render(request, 'posts/technote.html')

def dictionary(request):
    return render(request, 'posts/technote.html')

def researchers(request):
    return HttpResponse("<h1>I'll be</h1>")
