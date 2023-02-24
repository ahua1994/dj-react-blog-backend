from django.urls import path
from .views import *

urlpatterns = [
    path("create/", PostCreateView.as_view()),
    path("rud/<int:id>/", PostRUDView.as_view()),
    # path("edit/<int:id>/", PostEditView.as_view()),
    # path("delete/<int:id>/", PostDeleteView.as_view()),
    path("all/", PostListAllView.as_view()),
    path("myposts/", PostListFilteredView.as_view()),
    path("<int:pk>/", PostDetailView.as_view()), 
]
