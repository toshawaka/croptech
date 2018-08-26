from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('technote/', views.TechnoteListView.as_view(), name='technote'),
    path('technote/<int:pk>/', views.TechnoteDetailView.as_view(), name='technote_detail'),
    path('technote/tags/', views.TagListView.as_view(), name='tag_list'),
    path('technote/tags/<str:tag>/', views.TagView.as_view(), name='tag'),
    path('dictionary/', views.dictionary, name='dictionary'),
    path('researchers/', views.researchers, name='researchers'),
]
