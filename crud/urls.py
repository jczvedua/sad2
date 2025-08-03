from django.urls import path
from .views import *

urlpatterns = [
    path('items/', items_list, name='items'),
    path('create/', create_item_view, name='create_item'),
    path('edit/<int:item_id>/', edit_item_view, name='edit_item'),
    path('delete/<int:item_id>/', delete_item_view, name='delete_item'),
]
