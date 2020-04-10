from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogList(APIView):

    def get(self, request):
        BlogList = BlogPost.objects.all()
        serializer = BlogPostSerializer(BlogList, many=True)
        return Response(serializer.data)

    def post (self):
        pass     
