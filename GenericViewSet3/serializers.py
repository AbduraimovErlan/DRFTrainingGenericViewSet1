from rest_framework import serializers
from GenericViewSet2.models import Book2




class SerializersBook3(serializers.ModelSerializer):
    class Meta:
        model = Book2
        fields = '__all__'