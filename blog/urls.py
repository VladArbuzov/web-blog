from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from users import views as user_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.PostView.as_view(), name='home'),
    path('<int:pk>/',views.PostDetail.as_view(),name='post-detail'),
    path('review<int:pk>/', views.AddComments.as_view(), name='comments_add'),
    path('add_likes/<int:pk>/', views.AddLike.as_view(), name='add_like'),
    path('del_likes/<int:pk>/', views.DelLike.as_view(), name='del_like'),
    path('create', views.create, name='create'),
    path('edit_post/<int:pk>/', views.edit_post, name='edit_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)