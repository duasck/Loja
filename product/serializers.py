from rest_framework import serializers
from .models import product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        #fields = ['um campo', 'outro campo']