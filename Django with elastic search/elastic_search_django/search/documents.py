from django_elasticsearch_dsl import Document, fields, Index
# from django_elasticsearch_dsl.registries import registry

from .models import ElasticDemo

PUBLISHER_INDEX = Index('elastic_demo')

PUBLISHER_INDEX.settings(
    number_of_shards=1,
    number_of_replicas=1
)

# @registry.register_document
# class NewsDocument(Document):
#     class Index:
#         # Name of the Elasticsearch index
#         name = 'test_index'
#         # See Elasticsearch Indices API reference for available settings
#         settings = {'number_of_shards': 1,
#                     'number_of_replicas': 0}
#     class Django:
#         model = Post
#         fields = [
#             'title',
#             'id',
#             'description',
        # ]

@PUBLISHER_INDEX.doc_type
class News1Document(Document):
    id = fields.IntegerField(attr='id')
    fielddata=True
    title = fields.TextField(
        fields={
            'raw':{
                'type': 'keyword',
            }
            
        }
    )
    content = fields.TextField(
        fields={
            'raw': {
                'type': 'keyword',
                
            }
        },
    )
    class Django(object):
        model = ElasticDemo

# posts = Index('posts')

# @Pposts.doc_type
# class PostDocument(DocType):
#     class Meta:
#         model = Post
#     fields = [
#         'title',
#         'id',
#         'description',
#     ]