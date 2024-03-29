
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('blog/', views.blog, name='blog'),
    path('addpage/', views.add_page, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.show_post, name='post'),
    path('category/<slug:cat_slug>/', views.show_category, name='category'),
]