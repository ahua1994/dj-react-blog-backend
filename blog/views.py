from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import PermissionDenied
from .serializers import *

# Create your views here.


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        user = User.objects.get(id=self.request.user.id)
        return super().perform_create(serializer.save(author=user))


# class PostEditView(UpdateAPIView):
#     serializer_class = PostSerializer
#     lookup_field = "id"

#     def get_queryset(self):
#         return Post.objects.filter(id=self.kwargs["id"])


# class PostDeleteView(DestroyAPIView):
#     serializer_class = PostSerializer
#     lookup_field = "id"

#     def get_queryset(self):
#         return Post.objects.filter(id=self.kwargs["id"])
class PostRUDView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user != self.object.author:
            raise PermissionDenied("Not the owner of this post")
        return super().get(request, *args, **kwargs)

    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs["id"])


class PostListAllView(ListAPIView):
    queryset = Post.objects.all().order_by("published")
    serializer_class = PostSerializer


class PostListFilteredView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        qs = Post.objects.filter(author_id=self.request.user.id)
        return qs.order_by("published")


class PostDetailView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs["id"])
