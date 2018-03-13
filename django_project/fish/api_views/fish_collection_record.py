# coding=utf8
from rest_framework.response import Response
from rest_framework.views import APIView
from fish.models.fish_collection_record import FishCollectionRecord
from fish.serializers.fish_collection_serializer import \
    FishCollectionSerializer


class FishCollectionList(APIView):
    """
    List all fish collection
    """

    def get(self, request, *args):
        """Get the collection records.

        :param request: HTTP request object
        :type request: HttpRequest

        :param args: Positional arguments
        :type args: tuple

        :returns: URL
        :rtype: HttpResponse
        """
        fish_collections = FishCollectionRecord.objects.all()
        serializer = FishCollectionSerializer(fish_collections, many=True)
        return Response(serializer.data)
