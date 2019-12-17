from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from . import models
from .serializer import NewsSerializer


class NewsAPIView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        obj = models.News.objects.all().order_by('-created_at')
        serializer = NewsSerializer(obj, many=True)
        body_response = {
            "data": serializer.data,
            "message": "get all data success",
            "code": 200
        }
        return Response(body_response)


    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            body_response = {
                "data": serializer.data,
                "message": "object created",
                "code": 201
            }
            return Response(body_response)

        body_response = {
            "data": None,
            "message": "object invalid create",
            "code": 400
        }
        return Response(body_response)
