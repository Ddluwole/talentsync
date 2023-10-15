from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated
from .models import BlogPost
from .serializers import UserLoginSerializer, UserRegisterSerializer, BlogPostSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

class UserRegisterView(CreateAPIView):
    serializer_class = UserRegisterSerializer

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=serializer.validated_data['username'])
        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

class CreateBlogPostView(CreateAPIView):
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ListBlogPostsView(ListAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()

class RetrieveUpdateBlogPostView(RetrieveUpdateAPIView):
    serializer_class = BlogPostSerializer
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated]

class DeleteBlogPostView(DestroyAPIView):
    queryset = BlogPost.objects.all()
    permission_classes = [IsAuthenticated]
