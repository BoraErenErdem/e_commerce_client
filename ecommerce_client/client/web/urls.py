

from django.urls import path
from . import views


urlpatterns = [
    path('category/create', views.create, name='create'),

    path('', views.get_all_categories, name='categories'),

    path('category/<int:id>', views.get_categories_by_id, name='detail'),

    path('category/update/<int:id>', views.update, name='update'),

    path('category/delete/<int:id>', views.delete, name='delete')
]