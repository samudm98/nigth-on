from django.http import Http404
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from nigth_on.pubs.models import Pub, Comment
from nigth_on.pubs.serializers import PubDetailSerializer, PubSerializer, CommentSerializer


class ListPubs(APIView):

    def get(self, request):
        """
        :return: list of all pubs
        """
        pubs = Pub.objects.all()
        serializer = PubSerializer(pubs, many=True)
        return Response(serializer.data)


class DetailPub(APIView):

    def get_object(self, pk):
        try:
            return Pub.objects.get(pk=pk)
        except Pub.DoesNotExist:
            raise Http404

    def get(self, request, id):
        pub = self.get_object(id)
        serializer = PubDetailSerializer(pub)
        return Response(serializer.data)


class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

