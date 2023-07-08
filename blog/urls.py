from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.blog,name='Blog'),
    path('categorie/<int:categoria_id>',views.categorie,name='Categories'),
    path('post/<int:post_id>',views.post,name='Post'),
]

urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)