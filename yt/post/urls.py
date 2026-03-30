from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.index, name='index'),

    path('group_posts/', views.group_post_list, name='group_post_list'),

    path(
        'group/<slug:slug>/',
        views.group_post_detail
    ),
]