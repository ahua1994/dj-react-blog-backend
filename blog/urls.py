from django.urls import path
from .views import *

urlpatterns = [
    path("post/", PostCreateView.as_view()),
    path("rud/<int:id>/", PostRUDView.as_view()),
    path("all/", PostListAllView.as_view()),
    path("myposts/", PostListFilteredView.as_view()),
    path("<int:pk>/", PostDetailView.as_view()),
    path("comment/", CommentAddView.as_view()),
    path("like/", LikeAddView.as_view()),
    path("comment/all/", CommentListView.as_view()),
    path("like/all/", LikeListView.as_view()),
    path("comment/<int:pk>/", CommentRUDView.as_view()),
    path("like/<int:pk>/", LikeRDView.as_view()),
]
