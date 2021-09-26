from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index_note, name='index'),
    path('upload/', views.upload_note, name='upload-note'),
    path('update/<int:note_id>', views.update_note, name='update'),
    path('delete/<int:note_id>', views.delete_note, name='delete-note'),
    path('tags/delete/<int:tag_id>', views.delete_tag, name='delete-tag'),
    path('tags/', views.index_tag, name='tags'),
    path('sorted/<int:tag_id>', views.sorted_tag, name='sorted')
]
