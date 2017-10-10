from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializers
# Create your views here.
class HelloApiView(APIView):
    """Test API view"""

    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns list of APIViews features"""

        an_apiview = [
        'uses HTTP methods as function (get, post, put, patch , delete)',
        'It is similar to tradiotional django views',
        'Gives you the most control over logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})

    def post(self, request):
        """Create hello message with our name"""

        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            salary = serializer.data.get('salary')
            message = 'Hello {0} with salary {1}'.format(name, salary)
            return Response({'message':message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """Handles updating an object"""
        return Response({'method':'put'})

    def patch(self, request, pk=None):
        """patch request, only updates fields specified in the request"""
        return Response({'method':'patch'})

    def delete(self, request, pk=None):
        """Deletes an object"""
        return Response({'method':'delete'})
