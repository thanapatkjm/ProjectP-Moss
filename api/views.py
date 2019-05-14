from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import UserPoints

max_id = 7000000000000
min_id = 5000000000000
# Create your views here.
class get_user(APIView):
    def get(self,request):
        username = int(self.request.query_params.get('id'))
        if (username<=max_id and username>=min_id):
            try:
                print("11111111111")
                user = User.objects.get(username=username)
            except:
                print("2222222222")
                newUser = User.objects.create_user(username=username,password="password")
                thisUser = UserPoints.objects.create(user=newUser)
                data = {"id":username,
                        "verify":True,
                        "point(s)":thisUser.points}
            else:
                print("----------")
                print(user.id)
                thisUser = UserPoints.objects.get(user=user.id)
                thisUser.points = thisUser.points+1
                thisUser.save()
                data = {"id":username,
                        "verify":True,
                        "point(s)":thisUser.points}
        else:
            data = {"id":username,
                    "verify":False,
                    "error":"Invalid Id"}
        return Response(data)