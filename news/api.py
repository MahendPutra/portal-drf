from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SerializerNews
from .models import News


class NewsAPIView(APIView):
    serializer_class = SerializerNews

    def get(self, request):
        qs = News.objects.all()
        serializer = SerializerNews(qs, many=True)
        data = {
            'news': serializer.data,
            'message': 'get list data sukses'
        }
        return Response(data, status=status.HTTP_200_OK)


    def post(self, request):
        serializer = SerializerNews(data=request.data)
        if serializer.is_valid():
            serializer.save()

            data = {
                'news': serializer.data,
                'message': 'create list data sukses'
            }
            return Response(data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)