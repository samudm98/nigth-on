from rest_framework.serializers import ModelSerializer

from nigth_on.products.serializers import ProductSerializer
from nigth_on.pubs.models import Pub, ImageModel, Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ImagesSerializer(ModelSerializer):
    class Meta:
        model = ImageModel
        fields = '__all__'


class PubSerializer(ModelSerializer):
    images = ImagesSerializer()
    class Meta:
        model = Pub
        fields = '__all__'


class PubDetailSerializer(ModelSerializer):
    products = ProductSerializer(many=True)
    comments = CommentSerializer(many=True)
    images = ImagesSerializer(many=True)

    class Meta:
        model = Pub
        fields = '__all__'

