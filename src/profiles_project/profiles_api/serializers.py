from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
    """Serializes name fields for testing our APIView"""

    name = serializers.CharField(max_length=10)
    salary = serializers.FloatField(min_value=0)
