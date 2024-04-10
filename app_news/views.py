from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Author, Post, Comment
from .serializers import PostSerializer, PostShortSerializer, CommentSerializer


class MainView(APIView):

    def get(self, request):
        posts = Post.objects.all()[:100]
        serializer = PostShortSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)


class PostView(APIView):

    def get(self, request, id):
        print('post')
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, id):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
