import json

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import User
from .serializer import User_Serializer


class TGBotStart(APIView):

    def get(self, request):
        tel = request.query_params['phone']
        print(f"{tel}")

        try:
            user = User.objects.filter(telephone_number=tel)
            response_message = f"Hello {user[0].name}"
            return Response(response_message)
        except():
            return Response("ERROR")
