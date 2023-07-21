from rest_framework import serializers
from GenericViewSet5.models import Book5


class SerializersBook5(serializers.ModelSerializer):
    class Meta:
        model = Book5
        fields = '__all__'