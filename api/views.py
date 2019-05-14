from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response


max_id = 7000000000000
min_id = 5000000000000
# Create your views here.
class get_user(APIView):
    def get(self,request):
        username = int(self.request.query_params.get('id'))
        if (username<=max_id and username>=min_id):
            try:
                user = User.objects.get(username=username)
            except:
                User.objects.create_user(username=username,password="password")
                data = {"id":username,
                        "verify":True,
                        "point(s)":0}
            else:
                data = {"id":username,
                        "verify":True,
                        "point(s)":0}
        else:
            data = {"id":username,
                    "verify":False,
                    "error":"Invalid Id"}
        return Response(data)

