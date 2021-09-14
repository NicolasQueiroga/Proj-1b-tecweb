from django.urls import path
from . import views
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload-note'),
    path('update/<int:note_id>', views.update_note),
    path('delete/<int:note_id>', views.delete_note)
]
