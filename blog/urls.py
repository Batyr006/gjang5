from . import views
from django.urls import path
from .views import DeleteComment




urlpatterns = [path('', views.PostView.as_view()),
               path('<int:pk>/', views.PostDetail.as_view()),
               path('review/<int:pk>', views.AddComments.as_view(), name='add_comments'),
               path('<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
               path('<int:pk>/add_likes/', views.AddLike.as_view(), name='add_like'),
               path('<int:pk>/del_likes/', views.DelLike.as_view(), name='del_likes'),
               path('add_comment_like/<int:comment_id>/', views.AddCommentLike.as_view(), name='add_comment_like'),
               path('del_comment_like/<int:comment_id>/', views.DelCommentLike.as_view(), name='del_comment_like'),
               path('edit_comment/<int:comment_id>/', views.EditComment.as_view(), name='edit_comment'),
               path('delete_comment/<int:comment_id>/', DeleteComment.as_view(), name='delete_comment'),
               ]
