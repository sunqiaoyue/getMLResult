from rest_framework.response import Response
from rest_framework.views import APIView
from .predict import predictResult


class getMLResult(APIView):
    def post(self, request):
        result = predictResult(request)
        return Response(result)
