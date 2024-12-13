from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl.field import Keyword
from elasticsearch_dsl import field
from django_app.models.user.user import User

@registry.register_document
class UserDocument(Document):
    class Index:
        name = 'user'

    
    class Django:
        model = User
        fields = [
            'username',
            'last_name',
            'date_joined'
        ]