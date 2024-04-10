from rest_framework import serializers
from .models import Author, Comment, Post


class FilterReviewListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):

    def to_representation(self, instance):
        serializer = self.parent.parent.__class__(instance, context=self.context)
        return serializer.data


class CommentSerializer(serializers.ModelSerializer):
    replies = RecursiveSerializer(many=True, required=False)

    class Meta:
        model = Comment
        fields = '__all__'
        list_serializer_class = FilterReviewListSerializer


class PostSerializer(serializers.ModelSerializer):
    comments_count = serializers.IntegerField(source='comments.count')
    comments = CommentSerializer(source='comments.all', many=True)

    class Meta:
        model = Post
        depth = 2
        fields = '__all__'


class PostShortSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.name')

    class Meta:
        model = Post
        fields = ['title', 'rate', 'author', 'date']
