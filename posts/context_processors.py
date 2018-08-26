from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Count
from .models import Tag

def common(request):
    """どのテンプレートにも渡すデータの作成"""
    site = get_current_site(request)
    context = {
        # タグを紐付いた記事数順に取得。tag.num_postsで件数が取得可
        'tags': Tag.objects.annotate(
            num_posts=Count('technote')).order_by('-num_posts')[:5],
    }
    return context
