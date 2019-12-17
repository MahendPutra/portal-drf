from rest_framework.views import APIView





class NewsAPIView(APIView):
    def get 




# from django.shortcuts import render
# from django.views import View
# from django.http import JsonResponse
# from django.core import serializers
# from .models import News


# class WebService(View):
#     def get(self, request):

#         qs = News.objects.all()
#         data = {
#             'news': serializers.serialize('python', qs),
#             'message': 'get sukses disimpan'
#         }
#         return JsonResponse(data)


# class WebService1(View):
#     def get(self, request):
#         news = list()
#         qs = News.objects.all()

#         for dt in qs:
#             news.append({
#                 "title": dt.title,
#                 # "author": dt.author.username,
#                 "cover": dt.cover.url,
#                 "category": dt.category,
#                 "datetime": dt.created_at,
#             })

#         data = {
#             'news': news,
#             'message': 'get sukses disimpan'
#         }
#         return JsonResponse(data)