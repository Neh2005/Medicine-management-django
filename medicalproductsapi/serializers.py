from rest_framework import serializers
from products.models import MedicalProduct

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalProduct
        fields = '__all__'