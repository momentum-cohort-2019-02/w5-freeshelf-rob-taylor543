from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:pk>', views.category_list_view, name='category-list')
]
