import os
from rest_framework import serializers
from models.brand.models import Brand

class CreateUpdateCarSerializer(serializers.Serializer):
    name = serializers.CharField(help_text="`name` of Car ",allow_null=True,allow_blank=True,required=False)
    color = serializers.CharField(help_text="`color` of Car ",allow_null=True,allow_blank=True,required=False)
    logo = serializers.CharField(help_text="`logo` of Car ",allow_null=True,allow_blank=True,required=False)
    brand = serializers.IntegerField(help_text="category of post",required=False,allow_null=True)
    description = serializers.CharField(help_text="`description` of Car ",allow_null=True,allow_blank=True,required=False)

    @staticmethod
    def validate(data):
        if not "brand" in data:
            raise serializers.ValidationError("brand is required")
        if not data["brand"]:
            raise serializers.ValidationError("brand is required")
        brand = Brand.objects.filter(id= data["brand"]).first()
        if not brand:
            raise serializers.ValidationError("brand is not found")
        return data 

