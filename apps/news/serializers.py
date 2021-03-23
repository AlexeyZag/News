from .models import *
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Post
       fields = ['id', 'headline', ]


class CommentSerializer(serializers.HyperlinkedModelSerializer):
   class Meta:
       model = Comment
       fields = ['id', 'com_text', ]


