import imp
from django.shortcuts import render
from .models import Links
from .serializers import LinkSerializer
from rest_framework import generics

# Create your views here.

class PostListApi(generics.ListAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostCreateApi(generics.CreateAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDetailApi(generics.RetrieveAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostUpdateApi(generics.UpdateAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer


class PostDeleteApi(generics.DestroyAPIView):
    queryset = Links.objects.filter(active=True)
    serializer_class = LinkSerializer



