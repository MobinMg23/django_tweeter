from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl.field import Keyword
from elasticsearch_dsl import field
from django_app.models.tweet.tweet import Tweet


@registry.register_document
class TweetDocument(Document):
    class Index:
        name = 'tweets'


    class Django:
        model = Tweet
        fields = [
            'content',
            'hashtag',
            'created_at',
        ]

