from django.db import models

# Create your models here.

def _get_latest_post(queryset):
    return queryset.filter(is_public=True).order_by('-created_at')[:5]

class Tag(models.Model):
    name = models.CharField(max_length=70)
    def __str__(self):
        return self.name

class Technote(models.Model):
    title = models.CharField("タイトル", max_length=200, null=True)
    tag = models.ManyToManyField(Tag, blank=True, null=True)
    abstract = models.CharField('概要', max_length=200, null=True)
    key_words = models.CharField('キーワード', max_length=200, null=True)
    thumbnail = models.ImageField(upload_to='post_thumbnail/', blank=True, null=True)
    img1 = models.ImageField(upload_to='post_image/', blank=True, null=True)
    img2 = models.ImageField(upload_to='post_image/', blank=True, null=True)
    img3 = models.ImageField(upload_to='post_image/', blank=True, null=True)
    img4 = models.ImageField(upload_to='post_image/', blank=True, null=True)
    img5 = models.ImageField(upload_to='post_image/', blank=True, null=True)
    is_public = models.BooleanField("公開可能？", default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    content = models.TextField(null=True)
    def __str__(self):
        return self.title

class Dictionary(models.Model):
    title = models.CharField("タイトル", max_length=200, null=True)
    is_public = models.BooleanField("公開可能？", default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    content = models.TextField(null=True)
    def __str__(self):
        return self.title

class Researchers(models.Model):
    title = models.CharField("タイトル", max_length=200, null=True)
    thumbnail = models.ImageField(upload_to='post_thumbnail/', blank=True, null=True)
    is_public = models.BooleanField("公開可能？", default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    content = models.TextField(null=True)
    def __str__(self):
        return self.title
