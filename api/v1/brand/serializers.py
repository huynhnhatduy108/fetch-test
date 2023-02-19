from rest_framework import serializers


class CreateUpdateBrandSerializer(serializers.Serializer):
    name = serializers.CharField(help_text="`name` of Brand ",allow_null=True,allow_blank=True,required=False)

    @staticmethod
    def validate(data):
        return data
