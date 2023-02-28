from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView, RetrieveDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.exceptions import PermissionDenied
from .serializers import *

# Create your views here.


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        print("hello")
        user = User.objects.get(id=self.request.user.id)
        return super().perform_create(serializer.save(author=user))


class PostRUDView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
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
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Post.objects.filter(author_id=self.request.user.id)
        return qs.order_by("published")


class PostDetailView(ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        return Post.objects.filter(id=self.kwargs["id"])


class LikeAddView(CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class CommentAddView(CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class LikeRDView(RetrieveDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer


class CommentRUDView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
