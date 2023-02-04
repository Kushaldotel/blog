from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('blog/', views.blog, name='blog'),
    path('postcomment/', views.PostComment, name="postcomment"),

    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    # path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact'),
    path('home/', views.main, name="Ghar"),
]
