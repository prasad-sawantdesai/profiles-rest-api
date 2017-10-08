from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class HelloApiView(APIView):
    """Test API view"""

    def get(self, request, format=None):
        """Returns list of APIViews features"""

        an_apiview = [
        'uses HTTP methods as function (get, post, put, patch , delete)',
        'It is similar to tradiotional django views',
        'Gives you the most control over logic',
        'Is mapped manually to URLs'
        ]

        return Response({'message':'Hello!', 'an_apiview':an_apiview})
