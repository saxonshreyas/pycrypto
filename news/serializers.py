# this is necessary for defining the rest api to extract all the latest articles

from rest_framework import routers, serializers, viewsets
from .models import Article

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['uid', 'title', 'description', 'pub_date', 'link', 'publisher']