from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from GenericViewSet3.models import Book3
from GenericViewSet3.serializers import SerializersBook3




class GenericViewSetBook3(GenericViewSet):
    queryset = Book3.objects.all()
    serializer_class = SerializersBook3

    def list(self, request):
        serializers = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializers.data)

    def retrieve(self, request, pk):
        books = self.get_object()
        serializers = self.get_serializer(books)
        return Response(serializers.data)

    def create(self, request, *args, **kwargs):
        serializers = self.get_serializer(data=request.data)
        serializers.is_valid(raise_exception=True)
        serializers.save()
        return Response(serializers.data, status=status.HTTP_201_CREATED)


    def destroy(self, request, pk):
        books = self.get_object()
        books.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
